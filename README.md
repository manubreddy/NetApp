# NetApp
## Total Errors and CRC Errors

The "Total Errors and CRC Errors" script provides output with clearing counters on Cluster Node level commands.

### Usage

1. Edit the input file `TE.txt` or provide the detailed path of the file in the script's line 4.

   - The input file should have the output of the following command:
     ```
     system node run -node * -command ifstat -a
     ```

   - Modify the `TE.txt` file to contain the output of the above command, or specify the path to the file if it's located elsewhere.

2. Run the script to analyze the data in the input file.

This script allows you to collect and analyze error and CRC error data on cluster nodes by utilizing the output of the specified command.

### Example

Here's an example of how you can run the script:

```python
te_ce.py

