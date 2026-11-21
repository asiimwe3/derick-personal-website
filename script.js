const menu=document.querySelector('.menu');
const nav=document.querySelector('nav');
if(menu&&nav){
  menu.addEventListener('click',()=>{
    const open=nav.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(open));
  });
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded','false');
  }));
}
const year=document.getElementById('year');
if(year) year.textContent=new Date().getFullYear();

/* the quiet part: hidden by default, revealed on purpose */
(function(){
 var sec=document.getElementById('the-number');
 var open=document.getElementById('quietOpen');
 var close=document.getElementById('quietClose');
 if(!sec||!open) return;
 function show(smooth){
  sec.hidden=false;
  open.setAttribute('aria-expanded','true');
  if(smooth) sec.scrollIntoView({behavior:'smooth',block:'start'});
 }
 function hide(){
  sec.hidden=true;
  open.setAttribute('aria-expanded','false');
  open.scrollIntoView({behavior:'smooth',block:'center'});
 }
 open.addEventListener('click',function(){ show(true); });
 if(close) close.addEventListener('click',hide);
 var dot=document.getElementById('quietDot');
 if(dot) dot.addEventListener('click',function(e){ e.preventDefault(); show(true); });
 if(location.hash==='#the-number') show(false);
})();
