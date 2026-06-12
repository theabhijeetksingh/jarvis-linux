#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    try:
        from jarvis.core import Jarvis
        print("\n🤖 Starting Jarvis in text mode...\n")
        jarvis = Jarvis(mode="text", debug=False)
        jarvis.run()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down Jarvis...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
