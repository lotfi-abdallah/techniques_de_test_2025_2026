Module tp1.tests.test_perf
==========================
Performance tests for triangulation and binary serialization.

These tests are marked with @pytest.mark.perf so they can be excluded from
normal test runs using `pytest -m "not perf"`.

Functions
---------

`test_serialization_roundtrip_large()`
:   Measure serialization/deserialization throughput for a large pointset.

`test_triangulation_large_random()`
:   Measure triangulation speed on a moderately large random pointset.
    
    This test is marked `perf` so it can be excluded from normal test runs.
    It asserts the operation completes (no strict microsecond limits).