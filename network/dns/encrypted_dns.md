 1. [dns over tls vs dns over https](https://www.thesslstore.com/blog/dns-over-tls-vs-dns-over-https/)
 
  > From Joe
  > I really don’t see the problem or big deal here.
  > 
  > DoH seems clearly best for “Internet” traffic, so governements can’t block or see your traffic…
  > 
  > Or maybe they can anyway, because eventually ISPs will realize they can implement DoH themselves. After all they are both open standards and it is no good that only a few provide them.
  > 
  > So basically, when DoH get obiquitous enough, as regular DNS is today, Google & Cloudflare will be pressured to use the default system DNS settings. Most home users will not touch that and will use their ISPs DoH servers, privided by their routers DHCP. So the ISPs will (or can) again learn what sites their users go to, just like today. And just like today, ISPs will be preasured by most governements (even many of the suposedly “freedom” respecting ones), to give up that info to them.
  > 
  > China-like governments will probably block or prosecute users that don’t use their default ISP’s or whatever “sanctioned DoH prividers” they chose. So instead of the current Tor, users that care will need to have a local software in their browser or computer to use the regular ISP “sanctioned” DoH provider for the “approved” traffic, to pretend they are “obedient”, and for sensitive sites they will hit other DoH servers.
  > 
  > It is better than currently requiring Tor and alikes for privacy, but still for most users governements will by default be able to “see” their traffic, the same way they do now, via the ISPs.
  > 
  > On the other hand, DoT is clearly better for “company and VPN traffic” than DoH. So don’t use DoH inside your company, use DoT. I mean, why would you want to use DoH as a sysadmin over DoT?
  > 
  > Basically to resolve any internal IP you need to use the company provided DoT servers. There are NO DoH server available to you to use. So you just use those.
  > 
  > There is anyway now a push for zero trust security, moving away from VPNs and into all company services, even internal ones to be moved to publicly reachable HTTPS URLs. Those are authenticated sites that only properly identified users can access. In such a world DoT is not going to help as regular people can and probably will chose DoH, specially if they own and control their devices.
  > 
  > That is another important point for company traffic and company infosec policies. You can’t trust a device of a non employee at all. You can trust to a certain level a device of an employee, as that person probably doesn’t want to lose the job. But if you really need to trust a device, then you need to provide the employee with a device owned and controlled by the company, any configuiration that is not allowed (like playing with DNS settings) can be locked down or used to lock out the employee access….
  > … or again, you could just make sure your HTTPS services are properly protected and behind a proper Identity Provider (implemented by you preferably) with MFA and other countermeasures against identity theft, password loss or compromise, etc.

