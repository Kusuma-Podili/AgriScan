# AgriScan: Precision Agriculture Crop Recommendation & Soil Intelligence Platform

**AgriScan** is an enterprise-scale precision agriculture intelligence, satellite remote sensing, robotics telematics, post-harvest logistics, and carbon MRV platform. It integrates FAO-56 agronomic models, multi-model machine learning ensembles, meteorological data ingestion, site-specific nutrient management (SSNM), ISOBUS/CAN bus precision machinery control, RothC-26.3 soil organic carbon turnover, GS1 EPCIS cold-chain traceability, and actuarial crop insurance analytics.

---

## 🌟 Key Features & Enterprise Subsystems

### 1. Multi-Model Crop Recommendation Pipeline
- **Ensemble ML**: Combines LightGBM, XGBoost, CatBoost, and Deep Neural Networks (PyTorch) trained across extensive agro-climatic parameters.
- **Deterministic FAO EcoCrop Suitability Engine**: Mathematically gates recommendations against absolute and optimal physiological thresholds across 120+ crops.
- **Multi-Objective Optimization**: Ranks crops by combining suitability score (0–100%), predicted yield potential ($t/ha$), market price projections, and cultivation cost.

### 2. Satellite Remote Sensing & Phenology (`app.remote_sensing`)
- **Multi-Spectral Vegetation & Water Indices**: 25+ spectral indices (NDVI, NDRE, EVI, SAVI, MSAVI, NDWI, MNDWI, CIgreen, CIrededge, VARI, PRI, PSRI).
- **Sensor Calibration Catalogs**: Optical band radiometric calibrations for Sentinel-2 MSI, Landsat-9 OLI-2, PlanetScope SuperDove, and MicaSense RedEdge UAV.
- **Time-Series Smoothing**: Savitzky-Golay filtering and Whittaker smoothing for double-logistic phenological greenup, peak, and senescence detection.
- **Zonal Parcel Statistics**: Field boundary polygon raster extraction and vegetation vigor anomaly classifier.

### 3. Precision Agricultural Telematics & Robotics (`app.telematics`)
- **ISOBUS ISO 11783-10 Parser**: Task Controller XML parse tree, Process Data Variables, and 300+ DDI entity catalog.
- **SAE J1939 CAN Bus Telemetry**: High-frequency PGN decoders (EEC1, Fuel Economy, Ambient Conditions), PWM variable-rate nozzle duty cycles, and Dubins path guidance.
- **Machinery Fleet Database**: Detailed profiles of 250+ commercial tractors, combines, and precision implements.

### 4. Soil Nutrient & Health Diagnostics
- **Comprehensive Soil Analysis**: Evaluates primary macronutrients ($N, P, K$), secondary nutrients ($Ca, Mg, S$), micronutrients ($Zn, Fe, Mn, Cu, B$), and physical properties ($pH, EC$, organic carbon, soil texture classes).
- **Site-Specific Nutrient Management (SSNM)**: Balances elemental nutrient deficits into commercial fertilizer formulations (Urea, DAP, MOP, SSP, Zinc Sulphate) with growth-stage split schedules.

### 5. Post-Harvest Thermodynamics & Commodity Economics (`app.post_harvest`, `app.economics`)
- **Grain Drying Thermodynamics**: Modified Henderson equilibrium moisture content (EMC), Page thin-layer drying kinetics, and USDA storage life curves.
- **Global Commodity Pricing & Cash Markets**: 100+ global exchange futures contracts (CBOT, CME, Euronext, ICE, NCDEX) and 50 regional terminal market spot cash price series.

### 6. Controlled Environment Agriculture & Carbon MRV (`app.cea`, `app.carbon_mrv`)
- **Greenhouse Polyhouse Energy Balance**: Sensible and latent heat balance, pad-and-fan evaporative cooling, and supplemental DLI lighting controls.
- **Hydroponic Recipe Registry**: 100+ closed-loop ion concentration recipes (N, P, K, Ca, Mg, S, Fe, B, Mn, Zn, Cu, Mo, target EC and pH).
- **IPCC 2019 Tier 1/2 GHG Calculator**: Agricultural emissions accounting ($N_2O$ direct/indirect, enteric $CH_4$, flooded rice).
- **RothC-26.3 Soil Organic Carbon Simulator**: 5-pool carbon turnover model (DPM, RPM, BIO, HUM, IOM) with multi-annual climate decay coefficients.

### 7. Supply Chain Traceability & Actuarial Crop Insurance (`app.supply_chain`, `app.actuarial`)
- **GS1 EPCIS 2.0 Traceability Engine**: Harvest-to-retail batch lineage compliant with FDA FSMA 204 critical tracking events.
- **Cold Chain Kinetics**: Arrhenius shelf-life degradation equations and refrigerated container respiration heat load models.
- **Crop Insurance Actuarial Models**: Area-Yield Index Insurance (AYII), Weather-Index Insurance (WII) drought payout triggers, and Burning Cost rate calculations across 250+ agro-climatic peril zones.

### 4. Interactive Enterprise Dashboard & GIS
- **Parcel Polygon Mapping**: Leaflet-based field boundary digitizer, elevation contour overlays, and spatial soil sample heatmaps.
- **Interactive "What-If" Simulator**: Real-time slider-based scenario testing for water availability, rainfall projections, and fertilizer budgets.
- **Pest & Disease Microclimate Thermometer**: Predictive pest risk scoring based on real-time temperature-humidity thresholds.
- **PDF Advisory Exporter**: One-click printable soil health cards and agronomic advisory dossiers.

### 5. IoT Telemetry Gateway Simulator
- Virtual sensor telemetry streamer modeling soil moisture tension, electrical conductivity, and temperature probes with real-time Kalman filtering for noise reduction.

---

## 🏗️ System Architecture

```
agriscan/
├── backend/                  # FastAPI Application & Agronomic ML Engine
│   ├── app/
│   │   ├── api/              # RESTful API Endpoints (v1)
│   │   ├── core/             # Configuration, Database, Security & Logging
│   │   ├── models/           # SQLAlchemy ORM Data Entities
│   │   ├── schemas/          # Pydantic v2 Request/Response Schemas
│   │   ├── services/         # Domain Business Logic Orchestration
│   │   ├── ml/               # Machine Learning & Agronomy Engines
│   │   │   ├── classifiers/  # Random Forest, LightGBM, XGBoost, MLP
│   │   │   ├── agronomy/     # FAO EcoCrop, SSNM, Penman-Monteith, GDD
│   │   │   ├── pipeline/     # Preprocessing, Ensembling, Feature Engineering
│   │   │   └── data/         # 120+ Crop Profiles, Soil Taxonomy, Pest Matrices
│   │   ├── iot/              # Sensor Telemetry Simulator & Kalman Filtering
│   │   └── utils/            # GIS Geometry, PDF Generator, Unit Converters
│   └── tests/                # Comprehensive Pytest Backend Test Suite
├── frontend/                 # Vite + React 19 + TypeScript Platform
│   ├── src/
│   │   ├── components/       # Design System, GIS Maps, Soil Cards, Simulators
│   │   ├── services/         # API Integration Clients
│   │   ├── hooks/            # Custom React Hooks
│   │   ├── stores/           # Zustand Reactive State Stores
│   │   └── types/            # Domain TypeScript Definitions
│   └── tests/                # Vitest Component & Store Tests
├── scripts/                  # Data Seeders, Model Trainers, Benchmark Scripts
└── docker-compose.yml        # Multi-container orchestration (API, UI, Redis, DB)
```

---

## 🚀 Quickstart Guide

### Prerequisites
- Python 3.10 or higher
- Node.js 18+ and npm
- Docker & Docker Compose (optional for containerized deployment)

### 1. Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Interactive Swagger API documentation will be available at `http://localhost:8000/docs`.

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
The dashboard will be available at `http://localhost:5173`.

### 3. Docker Deployment
```bash
docker-compose up --build
```

---

## 🧪 Testing

### Running Backend Tests
```bash
cd backend
pytest -v --cov=app tests/
```

### Running Frontend Tests
```bash
cd frontend
npm run test
```


---

## 📡 REST API Quickstart & Examples

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

### Quick Crop Suitability Recommendation
```bash
curl -X POST "http://localhost:8000/api/v1/recommendations/quick" \
  -H "Content-Type: application/json" \
  -d '{
    "n_kg_ha": 135.0,
    "p_kg_ha": 45.0,
    "k_kg_ha": 40.0,
    "ph": 6.8,
    "organic_carbon_pct": 0.65,
    "ec_ds_m": 0.7,
    "temperature_c": 22.5,
    "temp_max_c": 28.0,
    "temp_min_c": 17.0,
    "humidity_pct": 65.0,
    "rainfall_mm": 550.0,
    "soil_texture": "loam",
    "top_k": 5
  }'
```
