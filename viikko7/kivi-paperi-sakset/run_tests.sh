#!/bin/bash

# Skripti testien ajamiseen

echo "======================================"
echo "Ajetaan unittest-testit..."
echo "======================================"
cd src
python -m unittest discover tests -v

echo ""
echo "======================================"
echo "Ajetaan Robot Framework API-testit..."
echo "======================================"
echo "Huom: Flask-serverin tulee olla käynnissä portissa 5000"
python -m robot tests/robot_api_tests.robot

echo ""
echo "======================================"
echo "Testit suoritettu!"
echo "======================================"
