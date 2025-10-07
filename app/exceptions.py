class CalculatorError(Exception):
    """Base exception for calculator errors."""

class ValidationError(CalculatorError):
    """Raised when input validation fails."""

class ConfigError(CalculatorError):
    """Raised when configuration is invalid."""

class OperationError(CalculatorError):
    """Raised for operation-specific errors (e.g., division by zero)."""
