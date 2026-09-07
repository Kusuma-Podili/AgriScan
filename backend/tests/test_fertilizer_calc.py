import pytest
from app.ml.agronomy.ssnm_fertilizer import SSNMEngine, SoilTestValues
from app.ml.data.crop_database import get_crop_by_id


def test_ssnm_nutrient_balance_calculation():
    """Verify SSNM nutrient demand, soil supply deduction, and recovery efficiency."""
    crop = get_crop_by_id("wheat")
    assert crop is not None

    soil = SoilTestValues(
        available_n_kg_ha=250.0,
        available_p2o5_kg_ha=20.0,
        available_k2o_kg_ha=150.0,
        organic_carbon_pct=0.55,
        ph=6.8,
        electrical_conductivity_ds_m=0.5,
        soil_texture="loam",
    )

    balance = SSNMEngine.calculate_nutrient_balance(crop, soil, target_yield_ton_ha=5.0)

    # 5.0 ton yield * 28 kg N/ton = 140 kg N demand
    assert pytest.approx(balance.total_demand_n_kg, rel=1e-2) == 140.0
    # Indigenous supply should be deducted
    assert balance.indigenous_supply_n_kg > 0
    assert balance.net_deficit_n_kg > 0
    # Fertilizer requirement should account for recovery efficiency (~40%)
    assert balance.fertilizer_requirement_n_kg > balance.net_deficit_n_kg


def test_ssnm_commercial_formulation_dap_urea_mop():
    """Verify conversion of elemental nutrients into commercial fertilizer bag quantities."""
    soil = SoilTestValues(
        available_n_kg_ha=220.0,
        available_p2o5_kg_ha=18.0,
        available_k2o_kg_ha=130.0,
        organic_carbon_pct=0.50,
        ph=7.0,
        electrical_conductivity_ds_m=0.6,
        soil_texture="loam",
    )

    schedule = SSNMEngine.generate_fertilizer_schedule(
        crop_id="maize",
        soil=soil,
        target_yield_ton_ha=6.0,
        strategy="dap_urea_mop",
    )

    assert len(schedule.doses) >= 3
    product_names = [d.product_name for d in schedule.doses]
    # Should include DAP, Potash, and Urea
    assert any("Di-Ammonium Phosphate" in name for name in product_names)
    assert any("Urea" in name for name in product_names)
    assert any("Muriate of Potash" in name for name in product_names)

    # All bag counts and application rates should be positive
    for dose in schedule.doses:
        assert dose.rate_kg_ha > 0
        assert dose.bags_50kg_ha > 0
        assert dose.estimated_cost_usd > 0
