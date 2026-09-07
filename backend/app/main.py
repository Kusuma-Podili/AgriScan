from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.core.config import settings
from app.core.logging import logger
from app.core.database import init_db
from app.api.v1.router import api_router


def create_application() -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app = FastAPI(
        title="AgriScan",
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url=None,
        description="AgriScan Precision Agriculture Decision Support Platform",
    )

    # Configure Cross-Origin Resource Sharing (CORS)
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Include REST API endpoints
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.on_event("startup")
    def on_startup():
        logger.info("Initializing AgriScan Database and Domain Models...")
        init_db()
        logger.info("AgriScan Platform successfully booted and ready to serve requests.")

    @app.get("/health", tags=["System"])
    def health_check():
        return {
            "status": "healthy",
            "service": "AgriScan Agricultural Decision Platform",
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
        }

    @app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
    def dashboard_ui():
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>AgriScan - Precision Agriculture Decision Support System</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
                body { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
            
                @media print {
                    header, footer, .tab-btn, #btn-run-rec, button { display: none !important; }
                    main { padding: 0 !important; }
                    .tab-content { display: block !important; }
                    .tab-content:not(#tab-recommendations) { display: none !important; }
                }
            </style>
        </head>
        <body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col antialiased">
            <!-- Top Header Navigation (Full Width End-to-End) -->
            <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-xs w-full">
                <div class="w-full px-4 sm:px-6 lg:px-8 xl:px-12 2xl:px-16 py-3.5 flex items-center justify-between">
                    <div class="flex items-center space-x-3.5">
                        <div class="h-11 w-11 rounded-xl bg-green-700 flex items-center justify-center text-white shadow-sm shadow-green-900/10">
                            <i class="fa-solid fa-seedling text-xl"></i>
                        </div>
                        <div>
                            <div class="flex items-center space-x-2">
                                <span class="text-xl font-extrabold tracking-tight text-slate-900">Agri<span class="text-green-700">Scan</span></span>
                                <span class="px-2.5 py-0.5 text-[11px] font-semibold rounded-md bg-green-50 text-green-800 border border-green-200">Decision Platform</span>
                            </div>
                            <p class="text-xs text-slate-500 font-medium">Precision Agronomic Decision Support & Farm Management</p>
                        </div>
                    </div>
                    
                    <div class="flex items-center space-x-4">
                        <div class="hidden sm:flex items-center space-x-2 text-xs text-slate-600 bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200">
                            <i class="fa-solid fa-calendar-days text-green-700"></i>
                            <span class="font-medium">Active Season: 2026-27</span>
                        </div>
                        <button onclick="window.print()" class="px-4 py-2 rounded-lg bg-green-700 hover:bg-green-800 text-white text-xs sm:text-sm font-semibold shadow-xs transition flex items-center space-x-2">
                            <i class="fa-solid fa-print"></i>
                            <span>Print Advisory</span>
                        </button>
                    </div>
                </div>
            </header>

            <!-- Main Content Container (Full Width End-to-End) -->
            <main class="w-full px-4 sm:px-6 lg:px-8 xl:px-12 2xl:px-16 py-6 space-y-6 flex-1">
                <!-- Welcome Banner & Project Workflow Overview -->
                <div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-xs space-y-6 w-full">
                    <div class="max-w-4xl space-y-2">
                        <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-green-50 border border-green-200 text-green-800 text-xs font-semibold">
                            <span class="h-2 w-2 rounded-full bg-green-600"></span>
                            <span>System Status: Fully Operational</span>
                        </div>
                        <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
                            Field Soil Diagnostics & Precision Crop Recommendation System
                        </h1>
                        <p class="text-sm text-slate-600 leading-relaxed">
                            AgriScan evaluates indigenous soil macronutrients, chemical reaction pH, and seasonal weather trends to generate crop suitability rankings, site-specific fertilizer split schedules, and disease risk advisories.
                        </p>
                    </div>

                    <!-- 4-Step Agronomic Workflow -->
                    <div class="pt-5 border-t border-slate-100">
                        <div class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center space-x-2">
                            <i class="fa-solid fa-network-wired text-green-700"></i>
                            <span>Standard Agronomic Operating Workflow</span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-1.5">
                                <div class="flex items-center justify-between">
                                    <span class="h-6 w-6 rounded-md bg-green-700 text-white font-bold text-xs flex items-center justify-center">1</span>
                                    <i class="fa-solid fa-vial text-slate-400 text-sm"></i>
                                </div>
                                <h2 class="font-bold text-sm text-slate-900">Soil & Weather Entry</h2>
                                <p class="text-xs text-slate-500">Collects soil lab chemical measurements (N, P, K, pH) and seasonal meteorology.</p>
                            </div>

                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-1.5">
                                <div class="flex items-center justify-between">
                                    <span class="h-6 w-6 rounded-md bg-green-700 text-white font-bold text-xs flex items-center justify-center">2</span>
                                    <i class="fa-solid fa-filter text-slate-400 text-sm"></i>
                                </div>
                                <h2 class="font-bold text-sm text-slate-900">Crop Suitability Gating</h2>
                                <p class="text-xs text-slate-500">Filters crops by physiological tolerance envelopes and suitability scoring.</p>
                            </div>

                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-1.5">
                                <div class="flex items-center justify-between">
                                    <span class="h-6 w-6 rounded-md bg-green-700 text-white font-bold text-xs flex items-center justify-center">3</span>
                                    <i class="fa-solid fa-scale-balanced text-slate-400 text-sm"></i>
                                </div>
                                <h2 class="font-bold text-sm text-slate-900">Nutrient Balancing (SSNM)</h2>
                                <p class="text-xs text-slate-500">Calculates exact commercial fertilizer quantities (Urea, DAP, MOP) by growth stage.</p>
                            </div>

                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-1.5">
                                <div class="flex items-center justify-between">
                                    <span class="h-6 w-6 rounded-md bg-green-700 text-white font-bold text-xs flex items-center justify-center">4</span>
                                    <i class="fa-solid fa-clipboard-check text-slate-400 text-sm"></i>
                                </div>
                                <h2 class="font-bold text-sm text-slate-900">Advisory Synthesis</h2>
                                <p class="text-xs text-slate-500">Outputs disease risk warnings, yield probability projections, and irrigation guides.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Navigation Tabs (Full Width) -->
                <div class="border-b border-slate-200 flex overflow-x-auto space-x-2 pb-2 w-full">
                    <button onclick="switchTab('recommender')" id="tab-btn-recommender" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-semibold transition bg-green-700 text-white shadow-xs flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-seedling"></i>
                        <span>Crop Recommendation</span>
                    </button>
                    <button onclick="switchTab('soil-ssnm')" id="tab-btn-soil-ssnm" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-medium transition bg-white hover:bg-slate-100 text-slate-600 border border-slate-200 flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-flask-vial text-slate-500"></i>
                        <span>Soil Health & SSNM</span>
                    </button>
                    <button onclick="switchTab('weather-et0')" id="tab-btn-weather-et0" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-medium transition bg-white hover:bg-slate-100 text-slate-600 border border-slate-200 flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-cloud-sun-rain text-slate-500"></i>
                        <span>Agro-Weather & ET₀</span>
                    </button>
                    <button onclick="switchTab('satellite')" id="tab-btn-satellite" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-medium transition bg-white hover:bg-slate-100 text-slate-600 border border-slate-200 flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-satellite text-slate-500"></i>
                        <span>Satellite Indices</span>
                    </button>
                    <button onclick="switchTab('telematics')" id="tab-btn-telematics" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-medium transition bg-white hover:bg-slate-100 text-slate-600 border border-slate-200 flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-tractor text-slate-500"></i>
                        <span>Machinery Telematics</span>
                    </button>
                    <button onclick="switchTab('insurance')" id="tab-btn-insurance" class="tab-btn px-4 py-2.5 rounded-lg text-sm font-medium transition bg-white hover:bg-slate-100 text-slate-600 border border-slate-200 flex items-center space-x-2 whitespace-nowrap">
                        <i class="fa-solid fa-shield-halved text-slate-500"></i>
                        <span>Parametric Insurance</span>
                    </button>
                </div>

                <!-- TAB 1: CROP RECOMMENDER -->
                <div id="tab-recommender" class="tab-content space-y-6 w-full">
                    <!-- Preset Selector Buttons -->
                    <div class="bg-white border border-slate-200 rounded-xl p-4 shadow-xs space-y-2 w-full">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Regional Field Presets:</span>
                        <div class="flex flex-wrap gap-2 pt-1">
                            <button onclick="applyPreset('wheat')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🌾 Wheat (Grain Belt)</span>
                            </button>
                            <button onclick="applyPreset('rice')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🍚 Rice (Lowland Paddy)</span>
                            </button>
                            <button onclick="applyPreset('corn')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🌽 Maize (Corn Belt)</span>
                            </button>
                            <button onclick="applyPreset('soybean')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🌱 Soybean (Legume)</span>
                            </button>
                            <button onclick="applyPreset('cotton')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🌿 Cotton (Black Clay)</span>
                            </button>
                            <button onclick="applyPreset('potato')" class="px-3.5 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 border border-slate-200 transition flex items-center space-x-1.5">
                                <span>🥔 Potato (Horticulture)</span>
                            </button>
                        </div>
                    </div>

                    <!-- End-to-End Desktop Layout: 12-Column Grid -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 xl:gap-8 w-full">
                        <!-- Input Form Card (4 Columns on Desktop) -->
                        <div class="lg:col-span-4 xl:col-span-4 2xl:col-span-3 bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
                            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                    <i class="fa-solid fa-sliders text-green-700"></i>
                                    <span>Field Parameters</span>
                                </h2>
                                <button onclick="resetInputs()" class="text-xs text-slate-500 hover:text-slate-800 font-medium transition">Reset</button>
                            </div>

                            <div class="space-y-3.5 text-sm">
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1">Available Nitrogen (N kg/ha)</label>
                                    <input id="inp-n" type="number" value="135" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                </div>
                                <div class="grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Phosphorus (P kg/ha)</label>
                                        <input id="inp-p" type="number" value="45" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Potassium (K kg/ha)</label>
                                        <input id="inp-k" type="number" value="40" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    </div>
                                </div>
                                <div class="grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Soil Reaction (pH)</label>
                                        <input id="inp-ph" type="number" step="0.1" value="6.8" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Soil Texture</label>
                                        <select id="inp-texture" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 text-xs shadow-xs">
                                            <option value="clay loam">Clay Loam</option>
                                            <option value="sandy loam">Sandy Loam</option>
                                            <option value="loam" selected>Loam</option>
                                            <option value="silt loam">Silt Loam</option>
                                            <option value="black cotton clay">Black Cotton Clay</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Mean Temp (°C)</label>
                                        <input id="inp-temp" type="number" step="0.1" value="18.5" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-slate-700 mb-1">Humidity (%)</label>
                                        <input id="inp-humidity" type="number" value="62" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-semibold text-slate-700 mb-1">Seasonal Rainfall (mm)</label>
                                    <input id="inp-rain" type="number" value="450" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                </div>
                            </div>

                            <button id="btn-run-rec" onclick="runRecommendation()" class="w-full py-3 px-4 rounded-xl bg-green-700 hover:bg-green-800 text-white font-bold transition shadow-xs flex items-center justify-center space-x-2">
                                <i class="fa-solid fa-calculator text-xs"></i>
                                <span>Generate Recommendation</span>
                            </button>
                        </div>

                        <!-- Results Presentation Panel (8 Columns on Desktop) -->
                        <div class="lg:col-span-8 xl:col-span-8 2xl:col-span-9 space-y-6">
                            <!-- Status Header -->
                            <div class="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between shadow-xs">
                                <div class="flex items-center space-x-2">
                                    <i class="fa-solid fa-chart-pie text-green-700"></i>
                                    <span class="text-sm font-bold text-slate-900">Crop Suitability Rankings & Diagnostics</span>
                                </div>
                                <span id="rec-status-badge" class="text-xs px-2.5 py-1 rounded-full bg-green-50 text-green-800 border border-green-200 font-semibold">Ready</span>
                            </div>

                            <!-- Crop Cards Grid (Spans across width) -->
                            <div id="crop-cards-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-4">
                                <div class="bg-white border border-slate-200 rounded-xl p-5 text-center text-slate-400 sm:col-span-2 md:col-span-3 xl:col-span-5 py-12 shadow-xs">
                                    <i class="fa-solid fa-wheat-awn text-3xl text-slate-300 mb-2"></i>
                                    <p class="text-sm text-slate-500">Click "Generate Recommendation" to view agronomic rankings.</p>
                                </div>
                            </div>

                            <!-- SSNM Fertilizer Schedule -->
                            <div id="ssnm-section" class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4 hidden w-full">
                                <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                    <h3 class="text-sm font-bold text-slate-900 flex items-center space-x-2">
                                        <i class="fa-solid fa-flask-vial text-green-700"></i>
                                        <span>Site-Specific Nutrient Management (SSNM) Plan</span>
                                    </h3>
                                    <span id="fert-strategy-tag" class="text-xs px-2.5 py-0.5 rounded-full bg-green-50 text-green-800 border border-green-200 font-medium">Standard Formulation</span>
                                </div>
                                <div class="overflow-x-auto w-full">
                                    <table class="w-full text-left text-xs">
                                        <thead>
                                            <tr class="border-b border-slate-200 text-slate-500 bg-slate-50/50">
                                                <th class="py-2.5 px-3 font-semibold">Growth Stage</th>
                                                <th class="py-2.5 px-3 font-semibold">Commercial Fertilizer</th>
                                                <th class="py-2.5 px-3 font-semibold">Rate (kg/ha)</th>
                                                <th class="py-2.5 px-3 font-semibold">50kg Bags / ha</th>
                                                <th class="py-2.5 px-3 font-semibold">Application Method</th>
                                            </tr>
                                        </thead>
                                        <tbody id="fert-table-body" class="divide-y divide-slate-100 text-slate-700">
                                        </tbody>
                                    </table>
                                </div>
                                <div id="soil-amendment-box" class="bg-amber-50 border border-amber-200 rounded-lg p-3 text-xs text-amber-800 hidden"></div>
                            </div>

                            <!-- Disease & Pest Alerts -->
                            <div id="pest-section" class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4 hidden w-full">
                                <h3 class="text-sm font-bold text-slate-900 flex items-center space-x-2 border-b border-slate-100 pb-3">
                                    <i class="fa-solid fa-shield-virus text-amber-700"></i>
                                    <span>Microclimatic Pest & Disease Risk Assessment</span>
                                </h3>
                                <div id="pest-cards-container" class="grid grid-cols-1 md:grid-cols-2 gap-3"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 2: SOIL HEALTH & SSNM CALCULATOR -->
                <div id="tab-soil-ssnm" class="tab-content space-y-6 hidden w-full">
                    <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6 w-full">
                        <div class="border-b border-slate-100 pb-3">
                            <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                <i class="fa-solid fa-flask-vial text-green-700"></i>
                                <span>Soil Nutrient Balancer & Chemical Amendment Calculator</span>
                            </h2>
                            <p class="text-xs text-slate-500 mt-1">Calculates indigenous soil nutrient supply (INS) vs crop uptake demand to determine exact commercial formulation quantities.</p>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Target Crop</label>
                                <select id="ssnm-crop" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    <option value="wheat">Wheat (Triticum aestivum)</option>
                                    <option value="rice">Rice (Oryza sativa)</option>
                                    <option value="corn" selected>Maize / Corn (Zea mays)</option>
                                    <option value="cotton">Cotton (Gossypium hirsutum)</option>
                                    <option value="sugarcane">Sugarcane (Saccharum officinarum)</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Target Yield (t/ha)</label>
                                <input id="ssnm-yield" type="number" step="0.5" value="6.5" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Soil Texture Class</label>
                                <select id="ssnm-texture" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                                    <option value="clay loam">Clay Loam</option>
                                    <option value="loam" selected>Medium Loam</option>
                                    <option value="sandy loam">Sandy Loam</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Soil N (kg/ha)</label>
                                <input id="ssnm-n" type="number" value="260" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Soil P₂O₅ (kg/ha)</label>
                                <input id="ssnm-p" type="number" value="22" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Soil K₂O (kg/ha)</label>
                                <input id="ssnm-k" type="number" value="180" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Soil pH</label>
                                <input id="ssnm-ph" type="number" step="0.1" value="7.4" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                        </div>

                        <button onclick="calculateSSNMManual()" class="py-2.5 px-5 rounded-lg bg-green-700 hover:bg-green-800 text-white font-semibold text-sm transition shadow-xs flex items-center space-x-2">
                            <i class="fa-solid fa-calculator"></i>
                            <span>Calculate Nutrient Balance Sheet</span>
                        </button>

                        <div id="ssnm-calc-results" class="bg-slate-50 border border-slate-200 rounded-xl p-5 space-y-4 hidden w-full">
                            <h3 class="text-sm font-bold text-slate-900">Computed Fertilizer Requisition</h3>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4" id="ssnm-balances-grid"></div>
                            <div id="ssnm-amendment-alert" class="p-3 rounded-lg bg-white border border-slate-200 text-xs text-slate-700"></div>
                        </div>
                    </div>
                </div>

                <!-- TAB 3: AGRO-WEATHER & ET0 -->
                <div id="tab-weather-et0" class="tab-content space-y-6 hidden w-full">
                    <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6 w-full">
                        <div class="border-b border-slate-100 pb-3">
                            <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                <i class="fa-solid fa-cloud-sun-rain text-green-700"></i>
                                <span>FAO-56 Penman-Monteith Evapotranspiration (ET₀) & Irrigation</span>
                            </h2>
                            <p class="text-xs text-slate-500 mt-1">Calculates daily reference evapotranspiration based on solar radiation, vapor pressure deficit, and aerodynamic resistance.</p>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Max Temp (°C)</label>
                                <input id="et-tmax" type="number" step="0.1" value="33.5" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Min Temp (°C)</label>
                                <input id="et-tmin" type="number" step="0.1" value="21.0" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Mean RH (%)</label>
                                <input id="et-rh" type="number" value="62" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Wind Speed (m/s)</label>
                                <input id="et-wind" type="number" step="0.1" value="2.4" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                        </div>

                        <button onclick="calculateET0()" class="py-2.5 px-5 rounded-lg bg-green-700 hover:bg-green-800 text-white font-semibold text-sm transition shadow-xs flex items-center space-x-2">
                            <i class="fa-solid fa-droplet"></i>
                            <span>Compute Reference ET₀</span>
                        </button>

                        <div id="et0-results" class="bg-slate-50 border border-slate-200 rounded-xl p-5 space-y-4 hidden w-full">
                            <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                                <div>
                                    <span class="text-xs text-slate-500 font-medium">Daily Reference Evapotranspiration (ET₀):</span>
                                    <p id="et0-val-display" class="text-2xl font-extrabold text-green-800 mt-0.5">4.82 mm/day</p>
                                </div>
                                <span class="text-xs px-2.5 py-1 rounded-full bg-green-100 text-green-800 border border-green-200 font-semibold">Standard FAO-56 Formulation</span>
                            </div>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-slate-500">Initial Stage (Kc = 0.40):</span>
                                    <p id="kc-initial" class="text-sm font-bold text-slate-800 mt-1">1.9 mm/day</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-slate-500">Mid-Season Peak (Kc = 1.15):</span>
                                    <p id="kc-mid" class="text-sm font-bold text-slate-800 mt-1">5.5 mm/day</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-slate-500">Late Maturation (Kc = 0.65):</span>
                                    <p id="kc-late" class="text-sm font-bold text-slate-800 mt-1">3.1 mm/day</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 4: SATELLITE VEGETATION INDICES -->
                <div id="tab-satellite" class="tab-content space-y-6 hidden w-full">
                    <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6 w-full">
                        <div class="border-b border-slate-100 pb-3">
                            <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                <i class="fa-solid fa-satellite text-green-700"></i>
                                <span>Satellite Optical Reflectance & Vegetation Index Simulator</span>
                            </h2>
                            <p class="text-xs text-slate-500 mt-1">Computes canopy vigor and moisture stress across standard optical sensor bands (Sentinel-2 / Landsat-9).</p>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <label class="block text-xs font-semibold text-slate-700 mb-1">NIR (Band 8): <span id="val-nir" class="text-green-700 font-bold">0.52</span></label>
                                <input id="slider-nir" type="range" min="0.05" max="0.9" step="0.01" value="0.52" oninput="updateIndices()" class="w-full accent-green-700">
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Red (Band 4): <span id="val-red" class="text-rose-700 font-bold">0.08</span></label>
                                <input id="slider-red" type="range" min="0.01" max="0.6" step="0.01" value="0.08" oninput="updateIndices()" class="w-full accent-rose-700">
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <label class="block text-xs font-semibold text-slate-700 mb-1">RedEdge (Band 5): <span id="val-re" class="text-teal-700 font-bold">0.24</span></label>
                                <input id="slider-re" type="range" min="0.02" max="0.7" step="0.01" value="0.24" oninput="updateIndices()" class="w-full accent-teal-700">
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <label class="block text-xs font-semibold text-slate-700 mb-1">SWIR (Band 11): <span id="val-swir" class="text-sky-700 font-bold">0.18</span></label>
                                <input id="slider-swir" type="range" min="0.02" max="0.7" step="0.01" value="0.18" oninput="updateIndices()" class="w-full accent-sky-700">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 pt-2">
                            <div class="bg-white border border-slate-200 rounded-xl p-4 text-center shadow-xs">
                                <span class="text-xs text-slate-500 uppercase font-semibold">NDVI (Canopy Vigor)</span>
                                <p id="idx-ndvi" class="text-2xl font-extrabold text-green-700 mt-1">0.73</p>
                                <span class="text-xs text-slate-600">Dense Green Biomass</span>
                            </div>
                            <div class="bg-white border border-slate-200 rounded-xl p-4 text-center shadow-xs">
                                <span class="text-xs text-slate-500 uppercase font-semibold">NDRE (Chlorophyll)</span>
                                <p id="idx-ndre" class="text-2xl font-extrabold text-teal-700 mt-1">0.37</p>
                                <span class="text-xs text-slate-600">Balanced Nitrogen</span>
                            </div>
                            <div class="bg-white border border-slate-200 rounded-xl p-4 text-center shadow-xs">
                                <span class="text-xs text-slate-500 uppercase font-semibold">EVI (Enhanced Vigor)</span>
                                <p id="idx-evi" class="text-2xl font-extrabold text-slate-800 mt-1">0.68</p>
                                <span class="text-xs text-slate-600">Atmosphere Corrected</span>
                            </div>
                            <div class="bg-white border border-slate-200 rounded-xl p-4 text-center shadow-xs">
                                <span class="text-xs text-slate-500 uppercase font-semibold">NDWI (Water Content)</span>
                                <p id="idx-ndwi" class="text-2xl font-extrabold text-sky-700 mt-1">0.49</p>
                                <span class="text-xs text-slate-600">Normal Leaf Turgor</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 5: MACHINERY TELEMATICS -->
                <div id="tab-telematics" class="tab-content space-y-6 hidden w-full">
                    <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6 w-full">
                        <div class="border-b border-slate-100 pb-3">
                            <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                <i class="fa-solid fa-tractor text-green-700"></i>
                                <span>ISOBUS Task Controller & Variable-Rate Spray Simulator</span>
                            </h2>
                            <p class="text-xs text-slate-500 mt-1">Calculates pulse-width modulation (PWM) nozzle duty cycles to maintain calibrated target application rates across field speeds.</p>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Tractor Speed (km/h)</label>
                                <input id="telem-speed" type="number" step="0.5" value="14.0" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Target Rate (L/ha)</label>
                                <input id="telem-rate" type="number" value="150" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Boom Width (m)</label>
                                <input id="telem-width" type="number" step="1.0" value="24.0" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Nozzle Spacing (cm)</label>
                                <input id="telem-spacing" type="number" value="50" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                        </div>

                        <button onclick="calculateTelematics()" class="py-2.5 px-5 rounded-lg bg-green-700 hover:bg-green-800 text-white font-semibold text-sm transition shadow-xs flex items-center space-x-2">
                            <i class="fa-solid fa-gauge-high"></i>
                            <span>Calculate PWM Nozzle Duty Cycle</span>
                        </button>

                        <div id="telem-results" class="bg-slate-50 border border-slate-200 rounded-xl p-5 space-y-3 hidden w-full">
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">Total Boom Flow:</span>
                                    <p id="telem-flow" class="text-xl font-bold text-slate-900 mt-1">84.0 L/min</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">PWM Solenoid Duty Cycle:</span>
                                    <p id="telem-pwm" class="text-xl font-bold text-green-700 mt-1">68.5%</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">ISOBUS Status:</span>
                                    <p class="text-xs font-bold text-slate-700 mt-2">DDI 0x00A1 TC-SC Active</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 6: PARAMETRIC CROP INSURANCE -->
                <div id="tab-insurance" class="tab-content space-y-6 hidden w-full">
                    <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6 w-full">
                        <div class="border-b border-slate-100 pb-3">
                            <h2 class="text-base font-bold text-slate-900 flex items-center space-x-2">
                                <i class="fa-solid fa-shield-halved text-green-700"></i>
                                <span>Parametric Weather-Index Drought Risk Simulator</span>
                            </h2>
                            <p class="text-xs text-slate-500 mt-1">Simulates objective indemnity settlements based on recorded rainfall deficits against policy strike levels.</p>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Insured Area (ha)</label>
                                <input id="ins-ha" type="number" value="50" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Max Sum Insured (₹/ha)</label>
                                <input id="ins-sum" type="number" value="50000" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Trigger Rainfall (mm)</label>
                                <input id="ins-trig" type="number" value="250" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-700 mb-1">Actual Rainfall (mm)</label>
                                <input id="ins-actual" type="number" value="160" class="w-full px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600 shadow-xs">
                            </div>
                        </div>

                        <button onclick="calculateInsurance()" class="py-2.5 px-5 rounded-lg bg-green-700 hover:bg-green-800 text-white font-semibold text-sm transition shadow-xs flex items-center space-x-2">
                            <i class="fa-solid fa-calculator"></i>
                            <span>Evaluate Parametric Settlement</span>
                        </button>

                        <div id="ins-results" class="bg-slate-50 border border-slate-200 rounded-xl p-5 space-y-3 hidden w-full">
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">Indemnity Payout Rate:</span>
                                    <p id="ins-payout-ha" class="text-xl font-bold text-rose-700 mt-1">₹30,000.00 / ha</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">Total Claim Settlement:</span>
                                    <p id="ins-total-claim" class="text-xl font-bold text-green-800 mt-1">₹15,00,000.00</p>
                                </div>
                                <div class="bg-white p-4 rounded-lg border border-slate-200">
                                    <span class="text-xs text-slate-500">Settlement Ratio:</span>
                                    <p id="ins-ratio" class="text-xl font-bold text-slate-800 mt-1">60.0%</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>

            <!-- Bottom Footer (Full Width End-to-End) -->
            <footer class="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-500 w-full">
                <div class="w-full px-4 sm:px-6 lg:px-8 xl:px-12 2xl:px-16 space-y-1">
                    <p class="font-semibold text-slate-700">AgriScan Decision Support System</p>
                    <p>Site-Specific Nutrient Management &bull; FAO EcoCrop Models &bull; Multi-Model Crop Suitability &bull; ISOBUS Telematics</p>
                </div>
            </footer>

            <script>
                // Tab Switching
                function switchTab(tabId) {
                    document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
                    document.querySelectorAll('.tab-btn').forEach(el => {
                        el.classList.remove('bg-green-700', 'text-white', 'shadow-xs');
                        el.classList.add('bg-white', 'text-slate-600', 'border', 'border-slate-200');
                    });
                    
                    const activeContent = document.getElementById('tab-' + tabId);
                    if (activeContent) activeContent.classList.remove('hidden');

                    const activeBtn = document.getElementById('tab-btn-' + tabId);
                    if (activeBtn) {
                        activeBtn.classList.remove('bg-white', 'text-slate-600', 'border', 'border-slate-200');
                        activeBtn.classList.add('bg-green-700', 'text-white', 'shadow-xs');
                    }
                }

                // Presets
                const presets = {
                    wheat: { n: 135, p: 45, k: 40, ph: 6.8, temp: 18.5, humidity: 62, rain: 450, texture: 'loam' },
                    rice: { n: 110, p: 38, k: 48, ph: 6.2, temp: 28.0, humidity: 82, rain: 1250, texture: 'clay loam' },
                    corn: { n: 155, p: 58, k: 75, ph: 6.5, temp: 24.0, humidity: 70, rain: 720, texture: 'loam' },
                    soybean: { n: 35, p: 65, k: 75, ph: 6.6, temp: 24.5, humidity: 68, rain: 680, texture: 'loam' },
                    cotton: { n: 120, p: 45, k: 50, ph: 7.4, temp: 29.5, humidity: 55, rain: 550, texture: 'black cotton clay' },
                    potato: { n: 175, p: 85, k: 145, ph: 5.8, temp: 17.5, humidity: 75, rain: 600, texture: 'sandy loam' }
                };

                function applyPreset(name) {
                    const p = presets[name];
                    if (!p) return;
                    document.getElementById('inp-n').value = p.n;
                    document.getElementById('inp-p').value = p.p;
                    document.getElementById('inp-k').value = p.k;
                    document.getElementById('inp-ph').value = p.ph;
                    document.getElementById('inp-temp').value = p.temp;
                    document.getElementById('inp-humidity').value = p.humidity;
                    document.getElementById('inp-rain').value = p.rain;
                    document.getElementById('inp-texture').value = p.texture;

                    // Automatically execute recommendation
                    runRecommendation();
                }

                function resetInputs() {
                    document.getElementById('inp-n').value = 135;
                    document.getElementById('inp-p').value = 45;
                    document.getElementById('inp-k').value = 40;
                    document.getElementById('inp-ph').value = 6.8;
                    document.getElementById('inp-temp').value = 18.5;
                    document.getElementById('inp-humidity').value = 62;
                    document.getElementById('inp-rain').value = 450;
                    document.getElementById('inp-texture').value = 'loam';
                }

                // Run Core Recommendation
                async function runRecommendation() {
                    const badge = document.getElementById('rec-status-badge');
                    const btn = document.getElementById('btn-run-rec');
                    badge.innerText = 'Evaluating Suitability...';
                    badge.className = 'text-xs px-2.5 py-1 rounded-full bg-amber-50 text-amber-800 border border-amber-200 font-semibold';
                    btn.disabled = true;

                    const payload = {
                        n_kg_ha: parseFloat(document.getElementById('inp-n').value) || 135,
                        p_kg_ha: parseFloat(document.getElementById('inp-p').value) || 45,
                        k_kg_ha: parseFloat(document.getElementById('inp-k').value) || 40,
                        ph: parseFloat(document.getElementById('inp-ph').value) || 6.8,
                        organic_carbon_pct: 0.65,
                        ec_ds_m: 0.7,
                        temperature_c: parseFloat(document.getElementById('inp-temp').value) || 18.5,
                        temp_max_c: (parseFloat(document.getElementById('inp-temp').value) || 18.5) + 5,
                        temp_min_c: (parseFloat(document.getElementById('inp-temp').value) || 18.5) - 5,
                        humidity_pct: parseFloat(document.getElementById('inp-humidity').value) || 62,
                        rainfall_mm: parseFloat(document.getElementById('inp-rain').value) || 450,
                        soil_texture: document.getElementById('inp-texture').value || 'loam',
                        top_k: 5
                    };

                    try {
                        const res = await fetch('/api/v1/recommendations/quick', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload)
                        });

                        if (!res.ok) throw new Error('Recommendation service error ' + res.status);
                        const data = await res.json();

                        renderRecommendationResults(data);
                        badge.innerText = 'Evaluation Complete';
                        badge.className = 'text-xs px-2.5 py-1 rounded-full bg-green-50 text-green-800 border border-green-200 font-semibold';
                    } catch (err) {
                        badge.innerText = 'Evaluation Error';
                        badge.className = 'text-xs px-2.5 py-1 rounded-full bg-rose-50 text-rose-800 border border-rose-200 font-semibold';
                        console.error(err);
                    } finally {
                        btn.disabled = false;
                    }
                }

                function renderRecommendationResults(data) {
                    const grid = document.getElementById('crop-cards-grid');
                    grid.innerHTML = '';

                    const ranks = data.crop_rankings || [];
                    ranks.forEach((crop, idx) => {
                        const isPrimary = (idx === 0);
                        const card = document.createElement('div');
                        card.className = `p-5 rounded-xl border transition shadow-xs ${
                            isPrimary ? 'bg-green-50/40 border-green-600/60 ring-1 ring-green-600/30' : 'bg-white border-slate-200 hover:border-slate-300'
                        }`;
                        
                        card.innerHTML = `
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-bold uppercase ${isPrimary ? 'text-green-800' : 'text-slate-500'}">Rank #${idx + 1} ${isPrimary ? '(Optimal)' : ''}</span>
                                <span class="text-xs px-2 py-0.5 rounded font-bold ${isPrimary ? 'bg-green-100 text-green-900 border border-green-200' : 'bg-slate-100 text-slate-700'}">${crop.composite_suitability_score}% Match</span>
                            </div>
                            <h3 class="text-base font-bold text-slate-900">${crop.crop_name}</h3>
                            <p class="text-xs text-slate-500 italic">${crop.scientific_name || ''}</p>
                            <div class="mt-3 pt-3 border-t border-slate-100 space-y-1.5 text-xs">
                                <div class="flex justify-between text-slate-600">
                                    <span>FAO Suitability:</span>
                                    <span class="font-semibold text-green-800">${crop.fao_suitability_class}</span>
                                </div>
                                <div class="flex justify-between text-slate-600">
                                    <span>Yield Estimate:</span>
                                    <span class="font-semibold text-slate-900">${crop.estimated_yield_ton_ha} t/ha</span>
                                </div>
                                <div class="flex justify-between text-slate-600">
                                    <span>Estimated Profit:</span>
                                    <span class="font-semibold text-green-700">₹${Math.round(crop.estimated_net_profit_usd_ha * 83).toLocaleString('en-IN')} / ha</span>
                                </div>
                            </div>
                        `;
                        grid.appendChild(card);
                    });

                    // Render SSNM Schedule
                    const ssnmSec = document.getElementById('ssnm-section');
                    const tbody = document.getElementById('fert-table-body');
                    const sched = data.top_crop_fertilizer_schedule;

                    if (sched && sched.doses) {
                        ssnmSec.classList.remove('hidden');
                        tbody.innerHTML = '';
                        sched.doses.forEach(d => {
                            const tr = document.createElement('tr');
                            tr.innerHTML = `
                                <td class="py-2.5 px-3 font-semibold text-slate-900">${d.timing_stage}</td>
                                <td class="py-2.5 px-3 text-green-800 font-semibold">${d.product_name}</td>
                                <td class="py-2.5 px-3 text-slate-700">${d.rate_kg_ha} kg/ha</td>
                                <td class="py-2.5 px-3 font-semibold text-slate-900">${d.bags_50kg_ha} bags</td>
                                <td class="py-2.5 px-3 text-slate-500">${d.application_method}</td>
                            `;
                            tbody.appendChild(tr);
                        });

                        const amendBox = document.getElementById('soil-amendment-box');
                        if (sched.soil_amendment_recommendation) {
                            amendBox.classList.remove('hidden');
                            amendBox.innerHTML = '<strong>Soil Amendment Advisory:</strong> ' + sched.soil_amendment_recommendation;
                        } else {
                            amendBox.classList.add('hidden');
                        }
                    }

                    // Render Pest Threats
                    const pestSec = document.getElementById('pest-section');
                    const pestCont = document.getElementById('pest-cards-container');
                    const pestData = data.top_crop_pest_alerts;

                    if (pestData && pestData.threats && pestData.threats.length > 0) {
                        pestSec.classList.remove('hidden');
                        pestCont.innerHTML = '';
                        pestData.threats.forEach(t => {
                            const isHigh = t.risk_category.includes('High') || t.risk_category.includes('Critical');
                            const div = document.createElement('div');
                            div.className = 'bg-slate-50 border border-slate-200 rounded-lg p-3.5 text-xs space-y-1';
                            div.innerHTML = `
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-slate-900">${t.name} (${t.organism_type})</span>
                                    <span class="px-2 py-0.5 rounded font-bold ${isHigh ? 'bg-rose-50 text-rose-800 border border-rose-200' : 'bg-amber-50 text-amber-800 border border-amber-200'}">${t.risk_category} (${t.risk_score_pct}%)</span>
                                </div>
                                <p class="text-slate-600">${t.active_symptoms}</p>
                                <p class="text-green-800 font-medium"><strong>Management Practice:</strong> ${t.recommended_ipm_measures.join('; ')}</p>
                            `;
                            pestCont.appendChild(div);
                        });
                    }
                }

                // Tab 2: Manual SSNM Calculator
                function calculateSSNMManual() {
                    const y = parseFloat(document.getElementById('ssnm-yield').value) || 6.0;
                    const sn = parseFloat(document.getElementById('ssnm-n').value) || 260;
                    const sp = parseFloat(document.getElementById('ssnm-p').value) || 22;
                    const sk = parseFloat(document.getElementById('ssnm-k').value) || 180;
                    const ph = parseFloat(document.getElementById('ssnm-ph').value) || 7.2;

                    const demN = y * 22.0;
                    const demP = y * 8.5;
                    const demK = y * 18.0;

                    const insN = sn * 0.35;
                    const insP = sp * 0.45;
                    const insK = sk * 0.50;

                    const reqN = Math.max(0, demN - insN);
                    const reqP = Math.max(0, demP - insP);
                    const reqK = Math.max(0, demK - insK);

                    const dapKg = reqP / 0.46;
                    const dapN = dapKg * 0.18;
                    const remN = Math.max(0, reqN - dapN);
                    const ureaKg = remN / 0.46;
                    const mopKg = reqK / 0.60;

                    document.getElementById('ssnm-calc-results').classList.remove('hidden');
                    const grid = document.getElementById('ssnm-balances-grid');
                    grid.innerHTML = `
                        <div class="bg-white p-4 rounded-lg border border-slate-200 shadow-xs">
                            <span class="text-xs text-slate-500 font-medium">Nitrogen Balance (Urea)</span>
                            <p class="text-xl font-bold text-slate-900 mt-1">${(ureaKg / 50).toFixed(1)} Bags/ha</p>
                            <span class="text-xs text-slate-500 font-semibold">${ureaKg.toFixed(1)} kg Urea (46% N)</span>
                        </div>
                        <div class="bg-white p-4 rounded-lg border border-slate-200 shadow-xs">
                            <span class="text-xs text-slate-500 font-medium">Phosphate Balance (DAP)</span>
                            <p class="text-xl font-bold text-slate-900 mt-1">${(dapKg / 50).toFixed(1)} Bags/ha</p>
                            <span class="text-xs text-slate-500 font-semibold">${dapKg.toFixed(1)} kg DAP (18-46-0)</span>
                        </div>
                        <div class="bg-white p-4 rounded-lg border border-slate-200 shadow-xs">
                            <span class="text-xs text-slate-500 font-medium">Potassium Balance (MOP)</span>
                            <p class="text-xl font-bold text-slate-900 mt-1">${(mopKg / 50).toFixed(1)} Bags/ha</p>
                            <span class="text-xs text-slate-500 font-semibold">${mopKg.toFixed(1)} kg MOP (60% K₂O)</span>
                        </div>
                    `;

                    const alertEl = document.getElementById('ssnm-amendment-alert');
                    if (ph > 8.0) {
                        alertEl.innerHTML = '<strong>Alkaline/Sodic Advisory:</strong> Soil pH is ' + ph + '. Apply 2.5 t/ha agricultural gypsum (CaSO₄·2H₂O) to restore exchangeable calcium.';
                    } else if (ph < 5.8) {
                        alertEl.innerHTML = '<strong>Soil Acidity Advisory:</strong> Soil pH is ' + ph + '. Apply 1.8 t/ha agricultural lime (CaCO₃) to restore optimal nutrient bioavailability.';
                    } else {
                        alertEl.innerHTML = '<strong>Optimal Reaction:</strong> Soil reaction pH ' + ph + ' is optimal for root nutrient bioavailability.';
                    }
                }

                // Tab 3: ET0 Calculator
                function calculateET0() {
                    const tmax = parseFloat(document.getElementById('et-tmax').value) || 32;
                    const tmin = parseFloat(document.getElementById('et-tmin').value) || 20;
                    const rh = parseFloat(document.getElementById('et-rh').value) || 60;
                    const wind = parseFloat(document.getElementById('et-wind').value) || 2.0;

                    const tmean = (tmax + tmin) / 2.0;
                    const delta = (4098 * (0.6108 * Math.exp((17.27 * tmean) / (tmean + 237.3)))) / Math.pow(tmean + 237.3, 2);
                    const gamma = 0.066;
                    const es = (0.6108 * Math.exp((17.27 * tmax) / (tmax + 237.3)) + 0.6108 * Math.exp((17.27 * tmin) / (tmin + 237.3))) / 2.0;
                    const ea = es * (rh / 100.0);
                    const rn = 14.5;
                    const g = 0.0;

                    const num = 0.408 * delta * (rn - g) + gamma * (900 / (tmean + 273)) * wind * (es - ea);
                    const den = delta + gamma * (1 + 0.34 * wind);
                    const et0 = Math.max(1.0, num / den);

                    document.getElementById('et0-results').classList.remove('hidden');
                    document.getElementById('et0-val-display').innerText = et0.toFixed(2) + ' mm/day';
                    document.getElementById('kc-initial').innerText = (et0 * 0.40).toFixed(1) + ' mm/day (' + (et0 * 0.40 * 7).toFixed(0) + ' mm/wk)';
                    document.getElementById('kc-mid').innerText = (et0 * 1.15).toFixed(1) + ' mm/day (' + (et0 * 1.15 * 7).toFixed(0) + ' mm/wk)';
                    document.getElementById('kc-late').innerText = (et0 * 0.65).toFixed(1) + ' mm/day (' + (et0 * 0.65 * 7).toFixed(0) + ' mm/wk)';
                }

                // Tab 4: Satellite Indices
                function updateIndices() {
                    const nir = parseFloat(document.getElementById('slider-nir').value);
                    const red = parseFloat(document.getElementById('slider-red').value);
                    const re = parseFloat(document.getElementById('slider-re').value);
                    const swir = parseFloat(document.getElementById('slider-swir').value);

                    document.getElementById('val-nir').innerText = nir.toFixed(2);
                    document.getElementById('val-red').innerText = red.toFixed(2);
                    document.getElementById('val-re').innerText = re.toFixed(2);
                    document.getElementById('val-swir').innerText = swir.toFixed(2);

                    const ndvi = (nir - red) / (nir + red);
                    const ndre = (nir - re) / (nir + re);
                    const evi = 2.5 * ((nir - red) / (nir + 6 * red - 7.5 * 0.05 + 1));
                    const ndwi = (nir - swir) / (nir + swir);

                    document.getElementById('idx-ndvi').innerText = ndvi.toFixed(2);
                    document.getElementById('idx-ndre').innerText = ndre.toFixed(2);
                    document.getElementById('idx-evi').innerText = evi.toFixed(2);
                    document.getElementById('idx-ndwi').innerText = ndwi.toFixed(2);
                }

                // Tab 5: Telematics
                function calculateTelematics() {
                    const spd = parseFloat(document.getElementById('telem-speed').value) || 12;
                    const rate = parseFloat(document.getElementById('telem-rate').value) || 150;
                    const width = parseFloat(document.getElementById('telem-width').value) || 24;

                    const totalFlow = (spd * width * rate) / 600.0;
                    const pwm = Math.min(100.0, Math.max(10.0, (totalFlow / 120.0) * 100.0));

                    document.getElementById('telem-results').classList.remove('hidden');
                    document.getElementById('telem-flow').innerText = totalFlow.toFixed(1) + ' L/min';
                    document.getElementById('telem-pwm').innerText = pwm.toFixed(1) + '%';
                }

                // Tab 6: Insurance
                function calculateInsurance() {
                    const ha = parseFloat(document.getElementById('ins-ha').value) || 50;
                    const maxPay = parseFloat(document.getElementById('ins-sum').value) || 50000;
                    const trig = parseFloat(document.getElementById('ins-trig').value) || 250;
                    const actual = parseFloat(document.getElementById('ins-actual').value) || 160;
                    const exit = 100.0;

                    let rate = 0;
                    if (actual < trig) {
                        rate = (trig - actual) / (trig - exit);
                        rate = Math.min(1.0, Math.max(0.0, rate));
                    }

                    const payHa = rate * maxPay;
                    const totalClaim = payHa * ha;

                    document.getElementById('ins-results').classList.remove('hidden');
                    document.getElementById('ins-payout-ha').innerText = '₹' + payHa.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' / ha';
                    document.getElementById('ins-total-claim').innerText = '₹' + totalClaim.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                    document.getElementById('ins-ratio').innerText = (rate * 100).toFixed(1) + '%';
                }

                // Auto-run initial recommendation on page load
                window.addEventListener('DOMContentLoaded', () => {
                    runRecommendation();
                });
            </script>
        </body>
        </html>
        """

    return app


app = create_application()
