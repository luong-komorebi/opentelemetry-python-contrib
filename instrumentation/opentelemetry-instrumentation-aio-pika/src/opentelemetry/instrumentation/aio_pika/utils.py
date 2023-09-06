from opentelemetry import context


def is_instrumentation_enabled() -> bool:
    return not context.get_value(
        "suppress_instrumentation"
    ) and not context.get_value(context._SUPPRESS_INSTRUMENTATION_KEY)
