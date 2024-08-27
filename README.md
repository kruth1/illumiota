# illumiota
A Python (12.0) program that can parse a file containing flow log data and maps each row to a tag based on a lookup table for am Illumio Technical Assessment.
Included are sample files provided that were used to test the program. To compile the program, please make sure needed files are included in directory before running.

## Prompt & Requirements
Write a program that can parse a file containing flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a csv file, and it has 3 columns, dstport,protocol,tag. The dstport and protocol combination decide what tag can be applied.  
- Input file as well as the file containing tag mappings are plain text (ascii) files  
- The flow log file size can be up to 10 MB 
- The lookup file can have up to 10000 mappings 
- The tags can map to more than one port, protocol combinations.  for e.g. sv_P1 and sv_P2 in the sample above. 
- The matches should be case insensitive
  
## Assumptions made
- The program only supports the default log format (version 2) where dstport is the 6th index and protocol is the 8th index.
- In addition to a lookup table and the flow logs, this program uses the [official IANA protocol numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) csv to parse the flow logs as needed by the output.
- The lookup table csv used is properly formatted with three columns
### Future improvements
- Having the output in csv/excel format would potentially make it more usable for any organization need
- Using the pandas library in addition could also benefit for additional future use cases

## Contact
Please reach out to Kruthi Kanduri at kkandurikruthi@gmail.com for additional questions or doubts.
