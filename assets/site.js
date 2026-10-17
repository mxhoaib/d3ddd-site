(function(){var C=window.D3DDD_CONFIG||{},E=C.EMAIL||'info@d3ddd.com';
var t=document.querySelector('.menu-toggle'),n=document.querySelector('.nav');if(t)t.onclick=function(){n.classList.toggle('open');t.setAttribute('aria-expanded',n.classList.contains('open'))};
document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});
var f=document.querySelector('form.enquiry');if(f)f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f);if(d.get('company_website'))return;
var L=document.documentElement.lang.indexOf('ar')===0,lab=L?['الاسم','الهاتف','البريد','الخدمة','التفاصيل']:['Name','Phone','Email','Service','Details'];
var body=[lab[0]+': '+(d.get('name')||''),lab[1]+': '+(d.get('phone')||''),lab[2]+': '+(d.get('email')||''),lab[3]+': '+(d.get('service')||''),'',lab[4]+':',(d.get('message')||'')].join('\n');
location.href='mailto:'+E+'?subject='+encodeURIComponent((L?'استفسار من الموقع – ':'Website enquiry – ')+(d.get('service')||''))+'&body='+encodeURIComponent(body)});
})();
