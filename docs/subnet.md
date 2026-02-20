# Subnet Sizing

    Classless Inter-Domain Routing (CIDR) is an IP address allocation method that improves data routing efficiency on the internet. 
 
    An IP address has two parts:
        • The network address is a series of numerical digits pointing to the network's unique identifier 
        • The host address is a series of numbers indicating the host or individual device identifier on the network
 
## About CIDR 
    CIDR Corresponds to number of network bits
        /N  →  number of bits used for the network portion
        
    An IPv4 address has 32 bits total.
        Network bits + Host bits = 32
        
    So:
    
    CIDR  Network bits	Host bits
    /22	22	10
    /28	28	4
    
    Host bits determine subnet size (THIS IS KEY)
 
### Usable IPs
    The number of usable IP addresses is: 2^(host bits)
    
    CIDR	Network bits	Host bits   Total IPs
    /22	22	10               1024
    /28	28	4                  16
    
    
    Less CIDR (network bits) = More host bits = larger subnet
    
    /22 --> 10 host bits → 2¹⁰ = 1024 IPs
    /28 --> 4 host bits → 2⁴ = 16 IPs
    
    Hence, /22 (Large subnet) > /28 (Small subnet)
