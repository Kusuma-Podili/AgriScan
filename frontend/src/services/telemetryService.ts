import { apiClient } from './apiClient';
import { SensorTelemetryPayload } from '../types/telemetry';

export const telemetryService = {
  async pollSensorTelemetry(sensorId: string): Promise<SensorTelemetryPayload> {
    return apiClient<SensorTelemetryPayload>(`/telemetry/poll/${sensorId}`);
  },

  async ingestTelemetry(payload: SensorTelemetryPayload): Promise<SensorTelemetryPayload> {
    return apiClient<SensorTelemetryPayload>('/telemetry/ingest', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },
};
