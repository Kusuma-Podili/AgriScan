"""
AgriScan GS1 EPCIS Agricultural Traceability and Batch Lineage Engine.
Complies with GS1 Electronic Product Code Information Services (EPCIS 2.0)
and FDA FSMA 204 Food Traceability Rule Critical Tracking Events (CTEs).
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class EPCISEventType(str, Enum):
    OBJECT_EVENT = "ObjectEvent"
    AGGREGATION_EVENT = "AggregationEvent"
    TRANSFORMATION_EVENT = "TransformationEvent"
    TRANSACTION_EVENT = "TransactionEvent"


class SupplyChainAction(str, Enum):
    ADD = "ADD"
    OBSERVE = "OBSERVE"
    DELETE = "DELETE"


class BusinessStep(str, Enum):
    HARVESTING = "urn:epcglobal:cbv:bizstep:harvesting"
    RECEIVING = "urn:epcglobal:cbv:bizstep:receiving"
    COOLING = "urn:epcglobal:cbv:bizstep:cooling"
    GRADING = "urn:epcglobal:cbv:bizstep:grading"
    PACKING = "urn:epcglobal:cbv:bizstep:packing"
    SHIPPING = "urn:epcglobal:cbv:bizstep:shipping"
    INSPECTING = "urn:epcglobal:cbv:bizstep:inspecting"
    RETAILING = "urn:epcglobal:cbv:bizstep:retailing"


class DispositionStatus(str, Enum):
    IN_PROGRESS = "urn:epcglobal:cbv:disp:in_progress"
    CONFORMING = "urn:epcglobal:cbv:disp:conforming"
    NON_CONFORMING = "urn:epcglobal:cbv:disp:non_conforming"
    IN_TRANSIT = "urn:epcglobal:cbv:disp:in_transit"
    RETAIL_SOLD = "urn:epcglobal:cbv:disp:retail_sold"
    DESTROYED = "urn:epcglobal:cbv:disp:destroyed"


class SensorReading(BaseModel):
    sensor_type: str
    reading_value: float
    uom: str
    recorded_at: datetime
    within_safe_threshold: bool


class EPCISEvent(BaseModel):
    event_id: str
    event_type: EPCISEventType
    action: SupplyChainAction
    business_step: BusinessStep
    disposition: DispositionStatus
    event_time: datetime
    read_point_gln: str
    biz_location_gln: str
    epc_list: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    child_epcs: List[str] = Field(default_factory=list)
    lot_number: Optional[str] = None
    crop_variety: Optional[str] = None
    quantity_kg: Optional[float] = None
    sensor_telemetry: List[SensorReading] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)


class TraceabilityChain(BaseModel):
    lot_number: str
    crop_name: str
    origin_farm_gln: str
    total_events: int
    events: List[EPCISEvent]
    provenance_verified: bool
    critical_temperature_excursions: int
    haccp_compliant: bool


class FarmTraceabilityEngine:
    """
    Manages end-to-end harvest-to-retail batch tracking and audits.
    """

    def __init__(self):
        self._events_by_lot: Dict[str, List[EPCISEvent]] = {}

    def register_event(self, event: EPCISEvent) -> None:
        if event.lot_number:
            if event.lot_number not in self._events_by_lot:
                self._events_by_lot[event.lot_number] = []
            self._events_by_lot[event.lot_number].append(event)

    def trace_batch(self, lot_number: str) -> Optional[TraceabilityChain]:
        if lot_number not in self._events_by_lot:
            return None

        evs = sorted(self._events_by_lot[lot_number], key=lambda x: x.event_time)
        if not evs:
            return None

        excursions = 0
        for ev in evs:
            for s in ev.sensor_telemetry:
                if not s.within_safe_threshold:
                    excursions += 1

        first = evs[0]
        haccp_ok = (excursions == 0)
        prov_ok = any(e.business_step == BusinessStep.HARVESTING for e in evs)

        return TraceabilityChain(
            lot_number=lot_number,
            crop_name=first.crop_variety or "Unknown Crop",
            origin_farm_gln=first.biz_location_gln,
            total_events=len(evs),
            events=evs,
            provenance_verified=prov_ok,
            critical_temperature_excursions=excursions,
            haccp_compliant=haccp_ok,
        )
