import os

from dotenv import load_dotenv

load_dotenv()

# Still working on discord-side triggering

# IMPORTANT! You must have a log for event reports and death leaderboards
# logs are achieved by using -logfile flag on launch, or by logging stdout
# Windows Users use forward slashes
file = os.getenv('LOG_FILE')

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Make sure are seen between server and script host
SERVER_ADDRESS = (os.getenv('VALHEIM_SERVER_IP'), int(os.getenv('VALHEIM_SERVER_PORT')))

# Shows up in embeds for stats report
SERVER_NAME = os.getenv('SERVER_NAME', 'Your server name')

# LOGCHAIN - where the bot outputs death and random mob events
LOGCHAN_ID = int(os.getenv('LOGCHAN_ID'))

# use a locked VC channel to report player count, if not, set as False
USEVCSTATS = os.getenv('USEVCSTATS') == 'True'

# VCHANNEL - where the bot shows server ticker, must be voice channel
VCHANNEL_ID = int(os.getenv('VCHANNEL_ID'))
