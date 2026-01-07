# CLAUDE.md - AI Assistant Guide

## Project Overview

This is an **ADS-B (Automatic Dependent Surveillance-Broadcast) Tracker** web application that displays real-time aircraft position data on an interactive map. The application fetches data from the OpenSky Network API and visualizes it using Leaflet.js.

**Technology Stack:**
- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript with Leaflet.js
- **Data Source**: OpenSky Network API
- **Map Provider**: OpenStreetMap

## Repository Structure

```
.
├── app.py                      # Flask application (main backend)
├── requirements.txt            # Python dependencies
├── README.md                   # User-facing documentation
├── static/
│   └── script.js              # Frontend JavaScript for map and data fetching
├── templates/
│   └── index.html             # Main HTML template with Leaflet map
└── .github/
    └── workflows/
        └── blank.yml          # GitHub Actions CI workflow (placeholder)
```

### File Descriptions

#### `app.py` (25 lines)
Main Flask application with two routes:
- `GET /` - Serves the main HTML page
- `GET /api/adsb` - Fetches ADS-B data from OpenSky Network API

**Key Features:**
- Error handling for network requests
- 5-second timeout on external API calls
- Returns JSON responses with error messages on failure
- Runs in debug mode on `0.0.0.0` (accessible from any network interface)

#### `static/script.js` (24 lines)
Frontend JavaScript that:
- Initializes Leaflet map centered at [0, 0] with zoom level 2
- Fetches data from `/api/adsb` endpoint
- Parses OpenSky Network API response format
- Places markers on map for each aircraft with latitude/longitude
- Binds aircraft callsign to marker popup

**OpenSky API Response Format:**
- `data.states` - Array of aircraft state vectors
- `state[5]` - Longitude
- `state[6]` - Latitude
- `state[1]` - Callsign

#### `templates/index.html` (18 lines)
Simple HTML page with:
- Leaflet CSS and JS loaded from CDN (v1.9.4)
- Map div with 600px height
- Title: "ADS-B Tracker"

#### `requirements.txt`
- Flask - Web framework
- requests - HTTP library for API calls

## Development Workflows

### Local Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

The application runs on `http://0.0.0.0:5000` with debug mode enabled.

### Testing the Application

1. **Manual Testing**: Open browser to `http://localhost:5000`
2. **API Testing**: Test endpoint directly at `http://localhost:5000/api/adsb`
3. **Network Failure Testing**: Application gracefully handles API failures

### Deployment Considerations

**Important Notes:**
- Debug mode is currently enabled in `app.py:25` - **MUST be disabled for production**
- No authentication on API endpoint
- No rate limiting implemented
- External API dependency (OpenSky Network) - may fail in restricted environments
- CORS not configured - may need adjustment for cross-origin requests

## Key Conventions & Patterns

### Backend Conventions

1. **Error Handling**: All external API calls wrapped in try/except blocks
2. **Timeouts**: 5-second timeout on external requests (app.py:18)
3. **JSON Responses**: All API endpoints return JSON format
4. **Host Configuration**: Binds to `0.0.0.0` for network accessibility

### Frontend Conventions

1. **Map Initialization**: Always center at [0, 0] with zoom level 2
2. **Data Fetching**: Single fetch on page load (no polling/refresh)
3. **Marker Creation**: One marker per aircraft with callsign popup
4. **CDN Usage**: Leaflet loaded from unpkg CDN

### Code Style

- **Python**: Standard Flask patterns, docstrings on route functions
- **JavaScript**: Modern async/await syntax, const declarations
- **HTML**: Minimal inline styles, external script loading

## Common Tasks for AI Assistants

### Adding New Features

When modifying this codebase:

1. **Backend Changes**: Modify `app.py` for new routes or API integrations
2. **Frontend Changes**: Update `static/script.js` for new map behaviors
3. **UI Changes**: Edit `templates/index.html` for layout modifications
4. **Dependencies**: Update `requirements.txt` for new Python packages

### Security Considerations

When working on this project, be aware of:

- **API Keys**: Currently no authentication - consider adding if deploying publicly
- **Input Validation**: No input sanitization - add if accepting user input
- **HTTPS**: External API uses HTTPS, ensure production deployment does too
- **Debug Mode**: Must be disabled in production (`app.py:25`)
- **XSS**: Callsign data is inserted into popups - ensure proper escaping if format changes

### Extending the API

To add new data sources:

1. Create new route in `app.py` following pattern of `/api/adsb`
2. Add error handling with try/except
3. Return JSON with consistent error format: `{'error': str(exc)}`
4. Update `script.js` to fetch from new endpoint
5. Document the expected data format in comments

### Testing Guidelines

Before committing changes:

1. **Verify Flask starts**: `python app.py` runs without errors
2. **Check API response**: `/api/adsb` returns valid JSON
3. **Test map rendering**: Markers appear on map (when data available)
4. **Check error handling**: Test with network disconnected
5. **Validate dependencies**: Ensure `requirements.txt` is complete

## Known Limitations

1. **No Real-time Updates**: Data fetched once on page load, no refresh mechanism
2. **No Marker Cleanup**: Markers accumulate, no removal of stale aircraft
3. **Limited Error Display**: API errors not shown to user on frontend
4. **No Filter/Search**: All aircraft displayed, no way to filter or search
5. **Basic CI**: GitHub Actions workflow is placeholder (blank.yml)

## Git Workflow

- **Main Branch**: Primary development branch (branch name not specified in git config)
- **Feature Branches**: Use `claude/*` prefix for AI assistant branches
- **Commit Messages**: Descriptive messages explaining the "why" not just "what"
- **Push Protocol**: Always use `git push -u origin <branch-name>`

## Environment Notes

- **Platform**: Linux 4.4.0
- **Python**: Compatible with Python 3.x
- **Network**: Requires internet access to fetch OpenSky API data
- **Port**: Default Flask development server on port 5000

## Future Enhancement Ideas

Consider these improvements when asked to extend functionality:

1. Auto-refresh aircraft data (polling or WebSockets)
2. Remove markers for aircraft that are no longer present
3. Display more aircraft information (altitude, speed, heading)
4. Add filtering by altitude, speed, or callsign
5. Implement proper CI/CD pipeline in blank.yml
6. Add unit tests for Flask routes
7. Add frontend tests for map functionality
8. Implement caching to reduce API calls
9. Add rate limiting to prevent API abuse
10. Create configuration file for API URL and other settings
11. Add logging for debugging and monitoring
12. Implement local data source fallback for restricted environments

## Contact & Documentation

- **Setup Instructions**: See README.md
- **API Documentation**: OpenSky Network API: https://opensky-network.org/api/
- **Leaflet Documentation**: https://leafletjs.com/reference.html
- **Flask Documentation**: https://flask.palletsprojects.com/

---

**Last Updated**: 2026-01-07
**Repository**: michaelkennedyau/playground
**Branch**: claude/claude-md-mk41g0nsex6f7iq6-nUDj5
