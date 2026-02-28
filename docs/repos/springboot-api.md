# springboot-api

[View on GitHub](https://github.com/msashish/springboot-api)

---

##  Create springboot project from
        https://start.spring.io/

##  For IntelliJ ensure Maven runner is set to proper JDK 
        jdk 1.8.0_212
        IntelliJ Idea > Preferences > Build tool > Maven > Runner  
        Else you will see error: No compiler is provided in this environment. Perhaps you are running on a JRE rather than a JDK)
          
##  Executing application 
        mvn clean install
        mvn dependency:tree -Dincludes=com.fasterxml.jackson.core
        mvn spring-boot:run 
        Check in postman GET http://localhost/library?name=Ashish  