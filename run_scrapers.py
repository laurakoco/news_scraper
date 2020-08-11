
from npr_scraper import *
from fox_scraper import *
from dailymail_scraper import *
from nyp_scraper import *
from cnn_scraper import *
from nyt_scraper import *
from reuters_scraper import *

# left
cnn_run()

# left-center
npr_run()
nyt_run()

# center
reuters_run()

# right-center
nyp_run()

# right
fox_run()
dm_run()