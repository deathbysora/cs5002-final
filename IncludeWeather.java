import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * This class reads each city and add the weather data of the destination and weather.
 */
public class IncludeWeather {
  
  /*
   * This class will loop though each entry. add visibility, wind speed to both origin and
   * destination at the time of the departure/arrival.
   */
  
  private static final int[] WEATHER_INDEX = new int[] {2, 4};
  
  private static Map<String, String[]> seaWeather;
  private static Map<String, String[]> ausWeather = new HashMap<>();
  private static Map<String, String[]> laxWeather = new HashMap<>();
  private static Map<String, String[]> jfkWeather = new HashMap<>();
  private static Map<String, String[]> miaWeather = new HashMap<>();
  private static Map<String, String[]> hnlWeather = new HashMap<>();
  
  // The main method to execute the code
  public static void main(String[] args) throws FileNotFoundException {
    
    // scan and build the weather data first
    File dir = new File("weather");
    File dirListing[] = dir.listFiles();
    
    File weather = new File ("weather/LAX_weather.csv");
    
    // Data structure:
    // Key: Date in form M/D/YY.
    // Value: String[] {Wind speed, Visibilities}
    seaWeather = new HashMap<>();
    ausWeather = new HashMap<>();
    laxWeather = new HashMap<>();
    jfkWeather = new HashMap<>();
    miaWeather = new HashMap<>();
    hnlWeather = new HashMap<>();
    
    if (dirListing != null) {
      
      for (File currentFile : dirListing) {
  
        Scanner weatherScan = new Scanner(currentFile);
        weatherScan.next();
        
        while (weatherScan.hasNext()) {
          String[] tokens = weatherScan.nextLine().split(",");
    
          switch (tokens[0]) {
            case "LAX":
              laxWeather.put(processDateWeather(tokens[1], false), new String[]{tokens[2], tokens[4]});
              break;
            case "SEA":
              seaWeather.put(processDateWeather(tokens[1], false), new String[]{tokens[2], tokens[4]});
              break;
            case "AUS":
              ausWeather.put(processDateWeather(tokens[1], false), new String[]{tokens[2], tokens[4]});
              break;
            case "JFK":
              jfkWeather.put(processDateWeather(tokens[1], false), new String[]{tokens[2], tokens[4]});
              break;
            case "MIA":
              miaWeather.put(processDateWeather(tokens[1], false), new String[]{tokens[2], tokens[4]});
              break;
            case "PHNL":
              hnlWeather.put(processDateWeather(tokens[1], true), new String[]{tokens[2], tokens[4]});
              break;
            default:
              System.out.println("No line found");
          }
        }
      }
    }
    
    // set up file systems for the master dataset
    File allEntries = new File("sortedData.csv");
    PrintStream output = new PrintStream(new File("sortedData_weather.csv"));
    Scanner entryScan = new Scanner(allEntries);
    
    // printout titles
    output.println(entryScan.nextLine()
            + ",ORIGIN_WIND_SPEED,ORIGIN_VISIBILITIES,DEST_WIND_SPEED,DEST_VISIBILITIES");
    
    // scan through the rest of the data and add in the weather data
    while (entryScan.hasNext()) {
      output.println(addWeatherData(entryScan.nextLine()));
    }
  }
  
  // it gets the input from sortedData regards to departure time/city, arrival time/city
  // and return (4) added data regards to:
  // Origin wind speed, origin visibilities, destination wind speed, destination visibilities
  private static String addWeatherData(String scan) {
    String output = scan; // original entry
    //System.out.println(scan);
    
    String[] tokens = scan.split(","); // break up the values
    
    //String[] datePlueMinute = tokens[0].split(" ");
    String[] date = tokens[0].split(" ")[0].split("/");
    
    
    String originCity = tokens[3];
    String destinationCity = tokens[4];
    
    String departureTime;
    String arrivalTime;
    
    // round up time to the nearest 5
    try {
      departureTime = roundUpOrDow(tokens[5]);
      arrivalTime = roundUpOrDow(tokens[7]);
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Incomplete Data!");
      return "";
    }
    
    // loop up the weather data from the maps
    String departureKey = tokens[0].split(" ")[0] + "," + departureTime;
    String arrivalKey = tokens[0].split(" ")[0] + "," + arrivalTime;
    
    String departureValue = weatherLookup(departureKey, originCity);
    String arrivalValue = weatherLookup(arrivalKey, destinationCity);
    
    
    return output + "," + departureValue + "," + arrivalValue;
  }
  
  private static String weatherLookup(String key, String city) {
    
    String output = ",";
    String[] value = null;
  
    try {
      switch (city) {
        case "LAX":
          value = laxWeather.get(key);
          return value[0] + "," + value[1];
    
        case "SEA":
          value = seaWeather.get(key);
          return value[0] + "," + value[1];
        //break;
        case "AUS":
          value = ausWeather.get(key);
          return value[0] + "," + value[1];
        //break;
        case "JFK":
          value = jfkWeather.get(key);
          return value[0] + "," + value[1];
        //break;
        case "MIA":
          value = miaWeather.get(key);
          return value[0] + "," + value[1];
        //break;
        case "PHNL":
          value = hnlWeather.get(key);
          return value[0] + "," + value[1];
        //break;
        default:
          System.out.println("No line found");
      }
    } catch (NullPointerException e) {
      System.out.println("No weather value found");
    }
    
    return output;
  }
  
  // process date format xx/xx/xx/ 00:00
  private static String processDateWeather(String inputDate, boolean isHnl) {
    
    String output = "";
    
    String[] datePlusMinute  = inputDate.split(" ");
    String[] time = datePlusMinute[1].split(":");
    String[] dateInput = datePlusMinute[0].split("-");
    
    String datePrint = Integer.parseInt(dateInput[1]) + "/" + Integer.parseInt(dateInput[2]) + "/" + dateInput[0].substring(2);
    int hourAdd;
    
    if (isHnl) {
      int hnlHour = Integer.parseInt(time[0]) - 10;
      hourAdd = Integer.parseInt(hnlHour + time[1]);
    } else {
      hourAdd = Integer.parseInt(time[0] + time[1]);
    }
    
    output = datePrint + "," + hourAdd;
    
    return output;
  }
  
  // will round up the departure time to the nearest 5 minute to match the data
  private static String roundUpOrDow(String timeEntry) {
    
    int time =  Integer.parseInt(timeEntry);
    int hour = time / 100;
    int minute = time % 100;
    
    int mod = minute % 5;
    
    if (mod < 3) {
      minute = minute - mod;
    } else {
      minute = minute + (5 - mod);
    }
    
    if (minute > 59) {
      minute = 0;
      hour++;
      
      if (hour == 24) {
        return 23 + "" + 55;
      }
      
      return hour + "00";
    }
    
    if (hour != 0) {
      if (minute / 10 == 0) {
        return hour + "0" + minute;
      } else {
        return hour + "" + minute;
      }
    } else {
      if (minute / 10 == 0) {
        return "0" + minute;
      } else {
        return "" + minute;
      }
    }
  }
}
