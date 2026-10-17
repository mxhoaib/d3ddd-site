(function(){var C=window.D3DDD_CONFIG||{};
var t=document.querySelector('.menu-toggle'),n=document.querySelector('.nav');if(t)t.onclick=function(){n.classList.toggle('open');t.setAttribute('aria-expanded',n.classList.contains('open'))};
document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});
var f=document.querySelector('form.enquiry');if(f&&C.FORM_ENDPOINT){f.addEventListener('submit',function(e){e.preventDefault();fetch(C.FORM_ENDPOINT,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}}).then(function(r){location.href='thank-you.html'}).catch(function(){alert('Could not send. Please email '+C.EMAIL)})})}
})();
