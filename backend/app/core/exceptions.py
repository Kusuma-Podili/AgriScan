from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class AgroPulseException(HTTPException):
    """Base exception for all domain-level errors in AgroPulse."""

    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class CropNotFoundError(AgroPulseException):
    def __init__(self, crop_id_or_name: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crop identifier or name '{crop_id_or_name}' not found in the agronomic database.",
        )


class SoilDataInvalidError(AgroPulseException):
    def __init__(self, reason: str):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid soil parameters provided: {reason}",
        )


class MeteorologicalDataUnavailableError(AgroPulseException):
    def __init__(self, location: str):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Meteorological or climate forecast data currently unavailable for coordinates/location: {reason}",
        )


class RecommendationEngineError(AgroPulseException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agronomic recommendation engine pipeline failed: {message}",
        )


class AuthenticationFailedError(AgroPulseException):
    def __init__(self, message: str = "Invalid authentication credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message,
            headers={"WWW-Authenticate": "Bearer"},
        )


class PermissionDeniedError(AgroPulseException):
    def __init__(self, message: str = "Operation not permitted for current user role"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=message,
        )
