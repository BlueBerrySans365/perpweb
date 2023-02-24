//This shit was made bc of fucking flask shit. So. Fuck it.

document.body.innerHTML = document.body.innerHTML.replaceAll('&lt;br&gt;', '<br>');
document.body.innerHTML = document.body.innerHTML.replaceAll('&lt;b&gt;', '<b>');
document.body.innerHTML = document.body.innerHTML.replaceAll('&lt;/b&gt;', '</b>');
document.body.innerHTML = document.body.innerHTML.replaceAll('&lt;BLYA&gt;', '                    ');
document.body.innerHTML = document.body.innerHTML.replaceAll("&lt;a href='/logout'&gt;Logout&lt;/a&gt;", "<a href='/logout'>Logout</a>")
document.body.innerHTML = document.body.innerHTML.replaceAll("&lt;a href='/login'&gt;Log in (via Discord)&lt;/a&gt;", "<a href='/login'>Log in (via Discord)</a>")
document.body.innerHTML = document.body.innerHTML.replaceAll("Fanart Contest", "<a href='https://youtu.be/yx1PZKTk0iA'>Fanart Contest</a>")
document.body.innerHTML = document.body.innerHTML.replaceAll("True_0", "&#10004;")
document.body.innerHTML = document.body.innerHTML.replaceAll("False_0", "&#10060;")