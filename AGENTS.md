# AGENTS.md

## Running Tests

This project uses `unittest` (Python standard library). No external dependencies are required.

### Run all tests

```bash
python3 -m unittest discover -v
```

### Run a specific test file

```bash
python3 -m unittest test_update_user -v
```

### Run an individual test

```bash
python3 -m unittest test_update_user.TestUpdateUser.test_successful_user_update_with_valid_data
```

## Notes

- Test files are located at the project root with the `test_` prefix.
- Commands must be run from the project root for imports to work correctly.
- No additional packages need to be installed; only Python 3 is required.
