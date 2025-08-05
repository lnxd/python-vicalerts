# Victoria Emergency Feed Poller

A Python package that polls the Victoria Emergency incidents feed, detects changes, and stores the complete history in SQLite.

## Features

- Polls the VicEmergency GeoJSON feed every 60 seconds
- Detects new events and field changes
- Stores complete feed history with compression
- Tracks individual event version history
- Uses conditional GET (ETag) to minimize bandwidth
- Graceful error handling with exponential backoff
- Rich CLI with progress display

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/python-vic_emergency_poller.git
cd python-vic_emergency_poller

# Create virtual environment with UV
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
uv pip install -e ".[dev]"
```

### From PyPI (when published)

```bash
uv pip install vicemergency
```

## Usage

### Command Line Interface

```bash
# Start continuous polling (default: every 60 seconds)
vicemergency run

# Run once and exit
vicemergency run --once

# Custom polling interval (minimum 10 seconds)
vicemergency run --interval 120

# Use custom database file
vicemergency run --db /path/to/custom.sqlite

# Disable progress display
vicemergency run --no-progress
```

### Additional Commands

```bash
# Show database statistics
vicemergency stats

# Show version history for a specific event
vicemergency history <event_id>
```

### Python API

```python
from vicemergency.poller import Poller

# Create poller with custom settings
poller = Poller(db_path="vicemergency.sqlite", interval=60)

# Run single poll
changes_detected = poller.run_once()

# Run continuous polling
poller.run()
```

## Database Schema

The SQLite database contains three tables:

- **feeds_raw**: Compressed raw feed snapshots with ETags
- **events**: One row per unique event (by sourceId)
- **event_versions**: Tracks every change to an event with timestamps

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/vicemergency --cov-report=term-missing

# Run specific test file
pytest tests/src/vicemergency/test_models.py
```

### Code Quality

```bash
# Format code
ruff format

# Check linting
ruff check --fix
```

## Data Source

This tool polls the Victoria Emergency public incidents feed:
https://emergency.vic.gov.au/public/events-geojson.json

## Attribution

© State of Victoria (EMV) — data licensed under CC BY 4.0 AU

## License

MIT License - see LICENSE file for details