# This script is needed for subprocess launched during tests;
# this way subprocess will not use prototype package from the site-packages directory
from prototype.prototypeapp import main
if __name__ == '__main__':
    main()
