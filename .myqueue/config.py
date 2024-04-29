# Generated with mq config.
#
# Please review the list of node types and remove those
# that you don't want to use.  Read more about config.py
# files here:
#
#   https://myqueue.readthedocs.io/en/latest/configuration.html

config = {
    'scheduler': 'lsf',
    'nodes': [
        ('XeonGold6342', {'cores': 48, 'memory': '504GB'}), 
        ('XeonGold6226R', {'cores': 32, 'memory': '378GB'}), 
        ('XeonGold6126', {'cores': 24, 'memory': '189GB'}), 
        ('XeonE5_2660v3', {'cores': 20, 'memory': '126GB'}), 
        ('XeonGold6142', {'cores': 32, 'memory': '378GB'}), 
        ('XeonE5_2650v4', {'cores': 24, 'memory': '252GB'})],
    'extra_args': ['-q', 'hpc']}
