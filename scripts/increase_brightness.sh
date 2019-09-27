#!/bin/bash
a=$(cat /sys/class/backlight/intel_backlight/brightness); echo $((a+5)) | sudo tee /sys/class/backlight/intel_backlight/brightness
