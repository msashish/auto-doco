# standalone-app

[View on GitHub](https://github.com/msashish/standalone-app)

---

## Basics and Setup

    Created using https://start.spring.io/ 
    
    For stand alone spring boot (non web), 
        StandaloneAppApplication implements CommandLineRunner 
        
    
    To build:
        mvn package
        
## To test
    java -jar target/standalone-app-0.0.1-SNAPSHOT.jar This is my first set of parameters
    mvn spring-boot:run -Dspring-boot.run.arguments=" Hello There!! How is the day today?"