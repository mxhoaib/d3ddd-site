/* D3DDD client portal: Supabase Auth when configured, otherwise DEMO mode in localStorage. */
(function(){
var C=window.D3DDD_CONFIG||{},DEMO=!(C.SUPABASE_URL&&C.SUPABASE_ANON_KEY&&window.supabase),sb=DEMO?null:window.supabase.createClient(C.SUPABASE_URL,C.SUPABASE_ANON_KEY);
var $=function(id){return document.getElementById(id)},page=location.pathname.split('/').pop()||'index.html';
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function msg(id,t,ok){var m=$(id);if(m){m.className='msg '+(ok?'ok':'err');m.textContent=t}}
if(DEMO&&$('demo-banner'))$('demo-banner').innerHTML='<p class="notice" style="margin-bottom:18px"><span class="demo-badge">DEMO</span> Demo mode: Supabase is not configured, so accounts and data are stored only in this browser (localStorage). Sample data is illustrative, not real projects. Do not enter real passwords.</p>';
/* ---------- DEMO backend ---------- */
var K='d3ddd_demo_',D={
 get:function(k,d){try{return JSON.parse(localStorage.getItem(K+k))||d}catch(e){return d}},set:function(k,v){localStorage.setItem(K+k,JSON.stringify(v))},
 signUp:async function(o){var u=D.get('users',{});if(u[o.email])throw Error('An account with this email already exists.');u[o.email]={pw:btoa(o.password),profile:{full_name:o.full_name,company:o.company,phone:o.phone,email:o.email}};D.set('users',u);D.seed(o.email);D.set('session',o.email)},
 signIn:async function(e,p){var u=D.get('users',{});if(!u[e]||u[e].pw!==btoa(p))throw Error('Invalid email or password.');D.set('session',e)},
 user:async function(){var e=D.get('session',null);return e?{id:e,email:e}:null},signOut:async function(){localStorage.removeItem(K+'session')},
 seed:function(e){var t=new Date().toISOString().slice(0,10);D.set('data_'+e,{projects:[{name:'Sample project (demo)',service:'Contractor Website',status:'In progress',updated_at:t}],files:[]})},
 data:function(e){return D.get('data_'+e,{projects:[],files:[]})},
 profile:async function(u){return D.get('users',{})[u.email].profile},saveProfile:async function(u,p){var x=D.get('users',{});Object.assign(x[u.email].profile,p);D.set('users',x)},
 list:async function(u,t){return D.data(u.email)[t]},
 upload:async function(u,f){if(f.size>1.5e6)throw Error('Demo mode stores files in the browser – max 1.5 MB.');var r=await new Promise(function(ok){var fr=new FileReader();fr.onload=function(){ok(fr.result)};fr.readAsDataURL(f)});var d=D.data(u.email);d.files.unshift({name:f.name,size:f.size,created_at:new Date().toISOString().slice(0,10),url:r});D.set('data_'+u.email,d)},
 reset:async function(){throw Error('Password reset is not available in demo mode.')}};
/* ---------- Supabase backend ---------- */
var S={
 signUp:async function(o){var r=await sb.auth.signUp({email:o.email,password:o.password,options:{data:{full_name:o.full_name,company:o.company,phone:o.phone},emailRedirectTo:location.origin+'/dashboard.html'}});if(r.error)throw r.error;return r.data},
 signIn:async function(e,p){var r=await sb.auth.signInWithPassword({email:e,password:p});if(r.error)throw r.error},
 user:async function(){var r=await sb.auth.getUser();return r.data.user},signOut:async function(){await sb.auth.signOut()},
 profile:async function(u){var r=await sb.from('profiles').select('*').eq('id',u.id).maybeSingle();return Object.assign({email:u.email},r.data||{})},
 saveProfile:async function(u,p){var r=await sb.from('profiles').upsert(Object.assign({id:u.id},p));if(r.error)throw r.error},
 list:async function(u,t){var q={projects:sb.from('projects').select('*').order('updated_at',{ascending:false}),files:sb.from('files').select('*').order('created_at',{ascending:false})}[t];var r=await q;if(r.error)throw r.error;
  if(t==='files')for(var f of r.data){var s=await sb.storage.from('client-files').createSignedUrl(f.path,3600);f.url=s.data&&s.data.signedUrl}return r.data},
 upload:async function(u,f){if(f.size>50e6)throw Error('Max 50 MB per file.');var path=u.id+'/'+Date.now()+'-'+f.name.replace(/[^\w.\-]/g,'_');var r=await sb.storage.from('client-files').upload(path,f);if(r.error)throw r.error;var i=await sb.from('files').insert({user_id:u.id,name:f.name,path:path,size:f.size,uploaded_by:'client'});if(i.error)throw i.error},
 reset:async function(e){var r=await sb.auth.resetPasswordForEmail(e,{redirectTo:location.origin+'/login.html'});if(r.error)throw r.error}};
var A=DEMO?D:S;
/* ---------- pages ---------- */
if($('signup-form'))$('signup-form').onsubmit=async function(e){e.preventDefault();try{var r=await A.signUp({full_name:$('sn').value.trim(),company:$('sc').value.trim(),phone:$('sph').value.trim(),email:$('se').value.trim().toLowerCase(),password:$('sp').value});
 if(!DEMO&&r&&!r.session){msg('msg','Account created. Check your email to confirm, then log in.',true);return}location.href='dashboard.html'}catch(x){msg('msg',x.message)}};
if($('login-form')){$('login-form').onsubmit=async function(e){e.preventDefault();try{await A.signIn($('le').value.trim().toLowerCase(),$('lp').value);location.href='dashboard.html'}catch(x){msg('msg',x.message)}};
 $('forgot').onclick=async function(e){e.preventDefault();var em=$('le').value.trim();if(!em)return msg('msg','Enter your email above first.');try{await A.reset(em);msg('msg','Password reset email sent.',true)}catch(x){msg('msg',x.message)}};
 A.user().then(function(u){if(u)location.href='dashboard.html'})}
if(page==='dashboard.html')(async function(){var u=await A.user();if(!u){location.replace('login.html');return}
 var p=await A.profile(u)||{};$('who').textContent=u.email;$('hello').textContent=p.full_name||u.email;$('pn').value=p.full_name||'';$('pc').value=p.company||'';$('pp').value=p.phone||'';$('pe').value=u.email;
 document.querySelectorAll('[data-tab]').forEach(function(b){b.onclick=function(){document.querySelectorAll('[data-tab]').forEach(function(x){x.classList.toggle('on',x===b)});document.querySelectorAll('.tab').forEach(function(t){t.classList.toggle('on',t.id==='t-'+b.dataset.tab)})}});
 $('logout').onclick=async function(){await A.signOut();location.href='login.html'};
 async function load(){var pr=[],iv=[],fl=[];try{pr=await A.list(u,'projects');fl=await A.list(u,'files')}catch(x){msg('file-msg','Could not load data: '+x.message)}
  $('proj-body').innerHTML=pr.length?pr.map(function(r){return'<tr><td>'+esc(r.name)+'</td><td>'+esc(r.service)+'</td><td><span class="badge">'+esc(r.status)+'</span></td><td>'+esc(String(r.updated_at||'').slice(0,10))+'</td></tr>'}).join(''):'<tr><td colspan=4>No projects yet.</td></tr>';
  $('file-body').innerHTML=fl.length?fl.map(function(r){return'<tr><td>'+esc(r.name)+'</td><td>'+Math.ceil((r.size||0)/1024)+' KB</td><td>'+esc(String(r.created_at||'').slice(0,10))+'</td><td>'+(r.url?'<a href="'+esc(r.url)+'" download="'+esc(r.name)+'"><u>Download</u></a>':'')+'</td></tr>'}).join(''):'<tr><td colspan=4>No files yet.</td></tr>';
  $('s-proj').textContent=pr.filter(function(r){return!/complete|cancel/i.test(r.status)}).length;$('s-files').textContent=fl.length}
 load();
 $('file-in').onchange=async function(){var f=this.files[0];if(!f)return;try{await A.upload(u,f);msg('file-msg','Uploaded '+f.name,true);this.value='';load()}catch(x){msg('file-msg',x.message)}};
 $('profile-form').onsubmit=async function(e){e.preventDefault();try{await A.saveProfile(u,{full_name:$('pn').value.trim(),company:$('pc').value.trim(),phone:$('pp').value.trim()});$('hello').textContent=$('pn').value;msg('prof-msg','Saved.',true)}catch(x){msg('prof-msg',x.message)}};
})();
})();
