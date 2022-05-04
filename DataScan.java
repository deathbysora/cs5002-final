import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * This class process the data and filter out any of the unnecessary entries.
 */
public class DataScan {
  /*
   * The  city should only contain: SEA JFK AUS HNL MIA LAX
   * The fields should only contain:
   *    date (FL_DATE), airline (OP_CARRIER), flight number (OP_CARRIER_FL_NUM)
   *    Departure city (ORIGIN), destination (DEST),
   *    departure time (DEP_TIME), DEP_DELAY, arrival time (ARR_TIME), ARR_DELAY
   *    [0, 1, 2, 3, 5, 8, 13]
   */
  private static final int[] REQUIRED_INDEX = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 11, 12};
  private static final String[] REQUIRED_CITY = new String[]{"SEA", "JFK", "AUS", "HNL", "MIA", "LAX"};
  
  public static void main(String[] args) throws FileNotFoundException {
    
    // set up file systems
    File allEntries = new File("2019_No_Cities.csv");
    PrintStream output = new PrintStream(new File("sortedData_1.csv"));
    Scanner entryScan = new Scanner(allEntries);
  
  
    String[] line = entryScan.nextLine().split(",");
    output.println(discardLines(line));
    
    // loop through all files
    while (entryScan.hasNext()) {
      // scan and write the first line
      line = entryScan.nextLine().split(",");
      
      // check if the plane is diverted
      int cancelledCode = Integer.parseInt(line[13]);
      
      // check if the origin and destination is the required city
      if (checkCities(line[3]) && checkCities(line[4]) && cancelledCode == 0) {
        output.println(discardLines(line));
      }
    }
  }
  
  private static String discardLines(String[] entry) {
    
    String output = entry[REQUIRED_INDEX[0]];
    
    // loop through and construct
    for (int i = 1; i < REQUIRED_INDEX.length; i++) {
      output += "," + entry[REQUIRED_INDEX[i]];
    }
    
    return output;
  }
  
  private static boolean checkCities(String city) {
    
    for (String c : REQUIRED_CITY) {
      if (city.equals(c)) {
        return true;
      }
    }
    
    return false;
  }
}
