#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Bean-Cup CLI entrypoint.
Invokes skills/visual-dashboard/scripts/manage_dashboard.py
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_SCRIPT = os.path.join(SCRIPT_DIR, "skills", "visual-dashboard", "scripts", "manage_dashboard.py")

if __name__ == "__main__":
    if not os.path.exists(DASHBOARD_SCRIPT):
        print(f"Error: {DASHBOARD_SCRIPT} not found.", file=sys.stderr)
        sys.exit(1)
    os.execv(sys.executable, [sys.executable, DASHBOARD_SCRIPT] + sys.argv[1:])
