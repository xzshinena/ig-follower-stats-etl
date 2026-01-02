See Instagram follower statistics

How to get the json files:
IG Profile -> Accounts Centre -> Your information and permissions -> Export your information -> Past activity -> Create export -> Export to device

Toggle settings for "Confirm your export"
- Customize Information -> only check 'Followers and following'
- Date Range -> All time
- Format -> json
- Media quality -> Low quality

You should recieve a zip file, two of the json files in it will separately hold list of all followers and list of all following
After importing file into workspace,
copy paths into src/sets.py
run python -m src.report
