Release Notes
-------------

**Future Releases**
    * Enhancements
        * Added common regression and time series regression datasets via git lfs :pr:`6`
        * Added ``MultiLayerPerceptronRegressor`` as a model :pr:`6`
        * Added nullable booleans, phone numbers, addresses, email addresses, URLs, currencies, file paths, full names, IPAddresses, and latitude/longitude as data types in ``Features`` :pr:`6`
        * Added ``Woodwork`` initialization for ``Features`` mock data :pr:`5`
        * Added ``Wave`` mock type :pr:`4`
        * Added convenience functions ``make_features``, ``make_dates``, and ``make_wave`` for making ``Features``, ``Dates``, and ``Wave`` mock types respectively :pr:`4`
        * Added ``Features``, ``Target``, and ``Dates`` mock types :pr:`3`
        * Added ``Scatter`` and ``Line`` graph types :pr:`3`
        * Added ``MockBase`` parent class :pr:`3`
        * Added ``GraphBase`` parent class :pr:`3`
        * Added ``create_data`` utility to make mock data creation easier :pr:`3`
        * Added ``handle_data_and_library_type`` and ``mock_dtypes`` helper functions :pr:`3`
    * Fixes
    * Changes
        * Removed ``Target`` mock data type :pr:`4`
    * Documentation Changes
        * Added and updated docstrings for a variety of classes and functions :pr:`4`
    * Testing Changes
        * Added and updated testing for subclasses :pr:`4`
    * CI/CD Changes
        * Added ``setup.py`` to enable the build process :pr:`3`
        * Added ``lint_tests`` GitHub Action to check for lint errors on PRs :pr:`3`
        * Added ``linux_unit_tests`` GitHub Action to check that all tests pass on PRs :pr:`3`
        * Added ``release_notes_updated`` GitHub Action to check that every PR is associated with an update in the release notes :pr:`3`
        * Added ``codecov`` support :pr:`3`

.. warning::

    **Breaking Changes**
