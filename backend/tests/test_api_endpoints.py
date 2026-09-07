import pytest
from fastapi.testclient import TestClient


def test_health_endpoint(client: TestClient):
    """Verify backend status health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_crop_catalog_endpoints(client: TestClient):
    """Verify crop catalog listing and filtering."""
    # List all crops
    res = client.get("/api/v1/crops/")
    assert res.status_code == 200
    crops = res.json()
    assert len(crops) >= 20

    # Filter by category
    res_cereals = client.get("/api/v1/crops/?category=Cereals")
    assert res_cereals.status_code == 200
    cereals = res_cereals.json()
    assert all(c["category"] == "Cereals" for c in cereals)

    # Get single crop profile
    res_single = client.get("/api/v1/crops/wheat")
    assert res_single.status_code == 200
    crop = res_single.json()
    assert crop["id"] == "wheat"
    assert crop["scientific_name"] == "Triticum aestivum"


def test_recommendations_run_endpoint(client: TestClient, auth_headers):
    """Verify end-to-end crop recommendation generation via REST API."""
    payload = {
        "n_kg_ha": 300.0,
        "p_kg_ha": 30.0,
        "k_kg_ha": 180.0,
        "ph": 6.5,
        "organic_carbon_pct": 0.65,
        "ec_ds_m": 0.7,
        "temperature_c": 27.0,
        "humidity_pct": 75.0,
        "rainfall_mm": 1200.0,
        "top_k": 5,
    }

    response = client.post("/api/v1/recommendations/run", json=payload, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()

    assert "crop_rankings" in data
    assert len(data["crop_rankings"]) == 5
    assert "top_crop_fertilizer_schedule" in data
    assert "top_crop_yield_risk_analysis" in data
    assert "top_crop_pest_alerts" in data


def test_weather_and_irrigation_endpoints(client: TestClient):
    """Verify weather current forecast and irrigation advisory endpoints."""
    res_weather = client.get("/api/v1/weather/current?latitude=21.0&longitude=78.0")
    assert res_weather.status_code == 200
    data = res_weather.json()
    assert len(data["forecast_7day"]) == 7
    assert data["et0_reference_mm_day"] > 0

    res_irrig = client.get("/api/v1/weather/irrigation-advisory?crop_id=wheat&soil_moisture_pct=22.0")
    assert res_irrig.status_code == 200
    irrig_data = res_irrig.json()
    assert irrig_data["crop_id"] == "wheat"
    assert "recommended_drip_runtime_hours" in irrig_data
