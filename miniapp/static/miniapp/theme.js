(() => {
  const tg=window.Telegram?.WebApp,root=document.documentElement;
  function apply(){
    const bg=tg?.themeParams?.bg_color;
    const backgroundDark=/^#[0-9a-f]{6}$/i.test(bg||'')?[1,3,5].reduce((n,i)=>n+parseInt(bg.slice(i,i+2),16),0)<384:null;
    const dark=tg?.colorScheme?tg.colorScheme==='dark':backgroundDark??matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.raptorTheme=dark?'dark':'light';root.style.setProperty('--raptor-wordmark',dark?'#fff':'#111');
    for(const [key,value] of Object.entries(tg?.themeParams||{}))if(/^#[0-9a-f]{6}$/i.test(value))root.style.setProperty('--tg-theme-'+key.replaceAll('_','-'),value);
  }
  window.raptorDisplayName=user=>{
    const clean=x=>!x||['null','undefined','none','@'].includes(String(x).trim().toLowerCase())?'':String(x).trim();
    const username=clean(user?.username).replace(/^@+/,'').trim();
    return username?'@'+username:clean(user?.first_name)||clean(user?.telegram_first_name)||clean(user?.name)||'';
  };
  window.raptorGreeting=user=>{const name=window.raptorDisplayName(user);return name?`Здравствуйте, ${name}!`:'Здравствуйте!';};
  apply();tg?.onEvent?.('themeChanged',apply);matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change',apply);
})();
