"""
One-time script to sync all existing data to Firebase
Run this after setting up Firebase sync service
"""

from database import sync_service

print("=" * 60)
print("  SYNCING ALL DATA TO FIREBASE")
print("=" * 60)

print("\nThis will sync all existing data from SQLite to Firebase.")
print("This is a one-time operation to initialize Firebase with existing data.\n")

input("Press Enter to continue...")

try:
    sync_service.sync_all_data()
    print("\n" + "=" * 60)
    print("  SYNC COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nAll data has been synced to Firebase.")
    print("Mobile app can now access this data.")
except Exception as e:
    print("\n" + "=" * 60)
    print("  SYNC FAILED!")
    print("=" * 60)
    print(f"\nError: {e}")
    print("\nPlease check:")
    print("1. Firebase credentials are correct")
    print("2. Internet connection is working")
    print("3. Firebase database is enabled")

