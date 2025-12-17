Module tp1.tests.test_api
=========================
API-level tests for the Triangulator HTTP endpoint.

Functions
---------

`test_communication_with_pointset_manager_failed_returns_503(client)`
:   Test that PointSetManager connection error returns 503.

`test_malformed_pointset_returns_400(client)`
:   Test that malformed binary returns 400 with error JSON.

`test_pointset_not_found_returns_404(client)`
:   Test that missing PointSet returns 404 with error JSON.

`test_triangulation_failure_returns_500(client)`
:   Test that triangulation exception returns 500 with error JSON.

`test_triangulation_happy_path(client)`
:   Test successful triangulation with valid PointSet ID.