#!/usr/bin/env bash
# pipenv shell
export ANDROID_BUILD=1
buildozer android debug deploy run logcat