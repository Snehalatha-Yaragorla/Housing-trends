function animate(id,val){
  let i=0;
  const el=document.getElementById(id);
  if(!el) return;

  const step=val/100;
  const t=setInterval(()=>{
    i+=step;
    if(i>=val){el.innerText=val.toLocaleString();clearInterval(t);}
    else el.innerText=Math.floor(i).toLocaleString();
  },20);
}

window.onload=()=>{
  animate("price",511619);
  animate("houses",21609);
  animate("renov",8000);
};
