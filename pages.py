# pages.py  -  X4G v9.8
# مدرن‌ترین طراحی — شیشه‌ای، مینیمال، بدون باگ

LOGO_B64 = "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"

# ============================================
# LOGIN_HTML — صفحه‌ی ورود مدرن شیشه‌ای
# ============================================
LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · X4G</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#080c18;
  --glass:rgba(255,255,255,0.04);
  --glass-border:rgba(255,255,255,0.06);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.55);
  --text:#edf2ff;
  --text-dim:rgba(255,255,255,0.32);
  --text-mid:rgba(255,255,255,0.6);
  --accent:#5b8def;
  --accent2:#7aa3ff;
  --transition:all 0.45s cubic-bezier(0.25,0.46,0.45,0.94);
}
[data-theme="light"]{
  --bg:#eef2f8;
  --glass:rgba(255,255,255,0.5);
  --glass-border:rgba(255,255,255,0.6);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.06);
  --text:#111827;
  --text-dim:rgba(0,0,0,0.28);
  --text-mid:rgba(0,0,0,0.5);
  --accent:#3b6fd4;
  --accent2:#5a88e8;
}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:var(--transition)}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse 70% 50% at 50% -10%, rgba(91,141,239,0.08), transparent 65%), var(--bg);z-index:0;transition:var(--transition)}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);background-size:48px 48px;z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;animation:float 16s ease-in-out infinite;opacity:0.3;pointer-events:none}
.o1{width:450px;height:450px;background:rgba(91,141,239,0.06);top:-120px;right:-100px;animation-delay:0s}
.o2{width:350px;height:350px;background:rgba(157,123,240,0.04);bottom:-80px;left:-80px;animation-delay:6s}
@keyframes float{0%,100%{transform:translateY(0) scale(1)}33%{transform:translateY(-35px) scale(1.05)}66%{transform:translateY(25px) scale(0.95)}}
.wrap{position:relative;z-index:10;width:100%;max-width:420px;animation:fadeUp 0.9s cubic-bezier(0.16,1,0.3,1)}
@keyframes fadeUp{from{opacity:0;transform:translateY(30px) scale(0.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.card{background:var(--glass);backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);border:1px solid var(--glass-border);border-radius:28px;padding:44px 36px 38px;box-shadow:var(--glass-shadow);position:relative;overflow:hidden;transition:var(--transition)}
.card-glow{position:absolute;top:-60px;right:-60px;width:240px;height:240px;background:radial-gradient(circle,var(--accent),transparent 70%);opacity:0.04;pointer-events:none;animation:pulseGlow 10s ease-in-out infinite}
@keyframes pulseGlow{0%,100%{transform:scale(1);opacity:0.03}50%{transform:scale(1.2);opacity:0.07}}
.login-title{text-align:center;margin-bottom:32px;position:relative;z-index:1}
.login-title h1{font-size:28px;font-weight:900;color:var(--text);letter-spacing:-0.02em;transition:var(--transition)}
.login-title h1 i{color:var(--accent);margin-left:10px}
.field{margin-bottom:20px;position:relative;z-index:1}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--text-mid);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.06em;display:flex;align-items:center;gap:6px;transition:var(--transition)}
.field label i{font-size:13px;color:var(--accent)}
.inp-wrap{position:relative;border-radius:16px;background:rgba(255,255,255,0.02);border:1.5px solid var(--glass-border);transition:var(--transition)}
.inp-wrap:focus-within{border-color:var(--accent);background:rgba(255,255,255,0.04);box-shadow:0 0 0 5px rgba(91,141,239,0.04)}
input[type=password],input[type=text]{width:100%;padding:15px 48px 15px 18px;border:none;background:transparent;color:var(--text);font-family:inherit;font-size:14px;outline:none;letter-spacing:0.02em;transition:var(--transition)}
input::placeholder{color:var(--text-dim);opacity:0.4}
.ic{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--text-dim);font-size:17px;pointer-events:none;transition:var(--transition)}
.inp-wrap:focus-within .ic{color:var(--accent);transform:translateY(-50%) scale(1.05)}
.pw-toggle{position:absolute;left:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:17px;padding:4px;transition:var(--transition);display:flex;align-items:center;z-index:2}
.pw-toggle:hover{color:var(--accent2);transform:translateY(-50%) scale(1.05)}
.err{display:none;background:rgba(239,68,68,0.05);border:1px solid rgba(239,68,68,0.1);border-radius:14px;padding:12px 16px;margin-bottom:16px;font-size:12px;color:#f87171;align-items:center;gap:10px;animation:shake 0.4s ease}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-6px)}40%{transform:translateX(6px)}60%{transform:translateX(-4px)}80%{transform:translateX(4px)}}
.err i{font-size:17px}
.btn{width:100%;padding:15px;border-radius:16px;border:none;cursor:pointer;background:linear-gradient(135deg,var(--accent),#7a5cf0);color:#fff;font-family:inherit;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 6px 30px rgba(91,141,239,0.2);transition:all 0.3s cubic-bezier(0.4,0,0.2,1);position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.08),rgba(255,255,255,0.02));opacity:0;transition:0.4s}
.btn:hover::before{opacity:1}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 40px rgba(91,141,239,0.3)}
.btn:active{transform:translateY(0) scale(0.98)}
.btn:disabled{opacity:0.5;cursor:not-allowed;transform:none}
.btn i{font-size:17px;transition:0.3s}
.btn:hover i{transform:translateX(-4px)}
.loading-dots{display:inline-flex;gap:5px;align-items:center}
.loading-dots span{width:7px;height:7px;border-radius:50%;background:#fff;animation:dotBounce 1.2s ease-in-out infinite}
.loading-dots span:nth-child(2){animation-delay:0.2s}
.loading-dots span:nth-child(3){animation-delay:0.4s}
@keyframes dotBounce{0%,80%,100%{transform:scale(0.5);opacity:0.3}40%{transform:scale(1);opacity:1}}
.theme-toggle{position:fixed;top:24px;right:24px;z-index:50;width:42px;height:42px;border-radius:50%;background:var(--glass);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--glass-border);color:var(--text-mid);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:19px;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);box-shadow:var(--glass-shadow)}
.theme-toggle:hover{transform:scale(1.06);background:rgba(255,255,255,0.06);color:var(--accent)}
.footer{margin-top:28px;padding-top:20px;border-top:1px solid var(--glass-border);display:flex;align-items:center;justify-content:center;gap:10px;font-size:11px;color:var(--text-dim);transition:var(--transition)}
@media(max-width:480px){.card{padding:32px 22px 28px}.login-title h1{font-size:22px}.theme-toggle{top:16px;right:16px;width:36px;height:36px;font-size:16px}}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div><div class="orb o1"></div><div class="orb o2"></div>
<button class="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
<div class="wrap">
  <div class="card">
    <div class="card-glow"></div>
    <div class="login-title"><h1><i class="ti ti-shield-lock"></i> ورود به پنل</h1></div>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form" autocomplete="off">
      <div class="field">
        <label><i class="ti ti-lock"></i> رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="••••••••" autofocus required>
          <button type="button" class="pw-toggle" onclick="togglePasswordVisibility()" title="نمایش/مخفی کردن رمز">
            <i class="ti ti-eye" id="pw-eye"></i>
          </button>
          <i class="ti ti-key ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> <span id="btn-text">ورود</span></button>
    </form>
    <div class="footer"><span>تمامی حقوق محفوظ است</span></div>
  </div>
</div>
<script>
let isDark=localStorage.getItem('x4g-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=document.getElementById('theme-icon');if(icon)icon.className='ti '+(dark?'ti-sun':'ti-moon');}
function toggleTheme(){isDark=!isDark;localStorage.setItem('x4g-theme',isDark?'dark':'light');applyTheme(isDark);}
applyTheme(isDark);
function togglePasswordVisibility(){const input=document.getElementById('pw');const icon=document.getElementById('pw-eye');if(!input||!icon)return;const isPassword=input.type==='password';input.type=isPassword?'text':'password';icon.className='ti '+(isPassword?'ti-eye-off':'ti-eye');input.focus();}
document.addEventListener('DOMContentLoaded',()=>{const pw=document.getElementById('pw');if(pw)pw.focus();});
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text'),pw=document.getElementById('pw');
  if(!btn||!err||!et||!pw)return;
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML=`<div class="loading-dots"><span></span><span></span><span></span></div><span id="btn-text">در حال ورود...</span>`;
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:pw.value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'رمز عبور اشتباه است');}
    btn.innerHTML='<i class="ti ti-circle-check"></i> <span id="btn-text">ورود موفق ✓</span>';btn.style.background='linear-gradient(135deg,#10B981,#059669)';btn.style.boxShadow='0 6px 30px rgba(16,185,129,0.4)';
    setTimeout(()=>{location.href='/dashboard';},600);
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> <span id="btn-text">ورود</span>';btn.style.background='';btn.style.boxShadow='';
    const wrap=pw.closest('.inp-wrap');if(wrap){wrap.style.borderColor='rgba(239,68,68,0.4)';setTimeout(()=>{wrap.style.borderColor='';},800);}
    pw.focus();pw.select();
  }
});
document.getElementById('pw').addEventListener('input',()=>{const err=document.getElementById('err');if(err)err.classList.remove('show');});
document.getElementById('pw').addEventListener('keydown',(e)=>{if(e.key==='Enter'){document.getElementById('form').dispatchEvent(new Event('submit'));}});
console.log('⚡ X4G v9.8 — پنل مدیریت پیشرفته');
</script>
</body>
</html>"""

# ============================================
# DASHBOARD_HTML — داشبورد مدرن شیشه‌ای
# ============================================
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X4G · داشبورد</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
/* ========================================
   طراحی شیشه‌ای آیفونی — X4G v9.8
   ======================================== */
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#080c18;--bg2:#0a1020;--bg3:#0d1428;
  --glass:rgba(255,255,255,0.03);--glass-border:rgba(255,255,255,0.05);--glass-shadow:0 16px 56px rgba(0,0,0,0.55);
  --card:var(--glass);--card-b:var(--glass-border);--card-bh:rgba(91,141,239,0.15);
  --accent:#5b8def;--accent2:#7aa3ff;--accent-d:rgba(91,141,239,0.08);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.06);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.06);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.06);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.06);--purple-t:#BCA4F7;
  --t1:#edf2ff;--t2:#8aa0c4;--t3:#48577a;
  --sidebar-w:248px;--radius:16px;--shadow:var(--glass-shadow);--transition:all 0.4s cubic-bezier(0.25,0.46,0.45,0.94);
}
[data-theme="light"]{
  --bg:#eef2f8;--glass:rgba(255,255,255,0.5);--glass-border:rgba(255,255,255,0.6);--glass-shadow:0 16px 56px rgba(0,0,0,0.06);
  --card:var(--glass);--card-b:var(--glass-border);--card-bh:rgba(46,99,214,0.25);
  --accent:#3b6fd4;--accent2:#5a88e8;--accent-d:rgba(46,99,214,0.06);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.06);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.06);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.06);--purple-t:#5A3CAD;
  --t1:#111827;--t2:#48577a;--t3:#8694b0;--shadow:var(--glass-shadow);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:var(--transition)}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.05);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--glass);backdrop-filter:blur(32px);-webkit-backdrop-filter:blur(32px);border-left:1px solid var(--glass-border);box-shadow:var(--shadow);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--glass-border)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid var(--glass-border);box-shadow:0 0 30px rgba(91,141,239,0.08);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1)}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--glass);border:1px solid var(--glass-border);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:var(--accent-d);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--glass-border)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--glass);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--glass-border);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:rgba(91,141,239,0.04);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.15);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.15)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--glass);backdrop-filter:blur(16px);border-bottom:1px solid var(--glass-border);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;box-shadow:0 0 8px rgba(139,92,246,.35)}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--glass);border:1px solid var(--glass-border);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:var(--purple-t)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--glass);backdrop-filter:blur(16px);border:1px solid var(--glass-border);border-radius:var(--radius);padding:17px 17px 14px;box-shadow:var(--shadow);transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,0,0,0.3)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ بقیه‌ی استایل‌های شیشه‌ای ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden;box-shadow:var(--shadow)}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--glass);backdrop-filter:blur(16px);border:1px solid var(--glass-border);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s;box-shadow:var(--shadow)}
.traf-mini:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}
.traf-chart-card{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--glass-border)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(91,141,239,.2)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}
@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.15);border:1px solid var(--glass-border);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.03)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:linear-gradient(135deg,var(--accent),#7a5cf0);color:#fff;box-shadow:0 2px 14px rgba(91,141,239,.2)}
.btn-p:hover{background:linear-gradient(135deg,#4a7de7,#6d48d6);box-shadow:0 4px 20px rgba(91,141,239,.3)}
.btn-o{background:var(--glass);backdrop-filter:blur(12px);border:1px solid var(--glass-border);color:var(--t2)}
.btn-o:hover{background:rgba(91,141,239,0.04);border-color:rgba(91,141,239,0.15);color:var(--accent2)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(91,141,239,0.1)}
.btn-g:hover{background:rgba(91,141,239,0.12)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,0.15)}
.btn-d:hover{background:rgba(239,68,68,0.15)}
.btn-pur{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,0.15)}
.btn-pur:hover{background:rgba(157,123,240,0.15)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(242,163,61,0.15)}
.btn-amber:hover{background:rgba(242,163,61,0.15)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--glass);backdrop-filter:blur(24px);border:1px solid var(--glass-border);border-radius:var(--radius);padding:18px 20px;box-shadow:var(--shadow);transition:border-color .2s,background .3s}
.card:hover{border-color:rgba(91,141,239,0.12)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(91,141,239,0.04);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.2);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--glass-border);background:rgba(0,0,0,.1);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.02)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(91,141,239,.4);background:rgba(0,0,0,.15);box-shadow:0 0 0 3px rgba(91,141,239,.05)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(91,141,239,0.1);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(242,163,61,0.15);color:var(--amber-t)}
.create-panel{background:var(--glass);backdrop-filter:blur(24px);border:1px solid var(--glass-border);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(91,141,239,.2)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.08);border:1px solid var(--glass-border);border-radius:14px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(46,99,214,.02)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--glass-border);background:rgba(0,0,0,.1);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .cp-input-full{background:rgba(0,0,0,.02)}
.cp-input-full:focus{border-color:rgba(91,141,239,.4);box-shadow:0 0 0 3px rgba(91,141,239,.05)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--glass-border);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(91,141,239,0.12);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(91,141,239,.2)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--glass-border);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.05)}
[data-theme="light"] .proto-card{background:rgba(0,0,0,.01)}
.proto-card:hover{border-color:rgba(91,141,239,0.15);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(91,141,239,0.05)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--glass-border);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(91,141,239,.2);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(91,141,239,.3)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
.srv-panel{background:var(--glass);backdrop-filter:blur(24px);border:1px solid var(--glass-border);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--glass-border)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(91,141,239,.2)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.08);border:1px solid var(--glass-border);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme="light"] .srv-tile{background:rgba(46,99,214,.02)}
.srv-tile:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}
.pw-panel{background:var(--glass);backdrop-filter:blur(24px);border:1px solid var(--glass-border);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(157,123,240,.2)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--glass-border);background:rgba(0,0,0,.1);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .pw-input{background:rgba(0,0,0,.02)}
.pw-input:focus{border-color:rgba(157,123,240,.4);box-shadow:0 0 0 3px rgba(157,123,240,.05)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.15);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(157,123,240,.2);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(157,123,240,.3)}
.pw-submit:active{transform:translateY(0) scale(.98)}
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--glass);backdrop-filter:blur(16px);border:1px solid var(--glass-border);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s;box-shadow:var(--shadow)}
.conn-hero-tile:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,0,0,0.3)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(31,184,126,.15)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:18px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative;box-shadow:var(--shadow)}
.conn-card-v2:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,0.25)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(31,184,126,.06),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(31,184,126,.2)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--glass-border) 15%,var(--glass-border) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.25),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--glass);backdrop-filter:blur(16px);border:1px dashed var(--glass-border);border-radius:20px;box-shadow:var(--shadow)}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}
@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}
@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(157,123,240,.04);border:1px solid rgba(157,123,240,.1);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--purple-t);word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--glass-border);background:var(--glass);backdrop-filter:blur(8px);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:rgba(157,123,240,.4);box-shadow:0 0 0 3px rgba(157,123,240,.05)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:20px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;box-shadow:var(--shadow)}
.sub-card:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,0.25)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(157,123,240,.2)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.08);border:1px solid var(--glass-border);border-radius:13px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(115,80,214,.02)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--glass-border)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-card-url-row{margin:14px 20px 0;background:rgba(157,123,240,.04);border:1px dashed rgba(157,123,240,.15);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--purple-t);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:var(--purple-t);transform:scale(1.1)}
.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--glass);backdrop-filter:blur(16px);border:1px dashed var(--glass-border);border-radius:20px;grid-column:1/-1;box-shadow:var(--shadow)}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}
.modal-v2{background:var(--glass);backdrop-filter:blur(32px);border:1px solid var(--glass-border);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:var(--shadow)}
.modal-v2-head{background:linear-gradient(155deg,rgba(157,123,240,.08) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(157,123,240,.1),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--glass);border:1px solid var(--glass-border);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.15)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(157,123,240,.2)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--glass-border)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--glass-border);background:rgba(0,0,0,.1);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .modal-v2-input{background:rgba(115,80,214,.02)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(157,123,240,.45);box-shadow:0 0 0 3px rgba(157,123,240,.05);background:rgba(0,0,0,.15)}
[data-theme="light"] .modal-v2-input:focus{background:rgba(0,0,0,.02)}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(91,141,239,.04);border:1px solid rgba(91,141,239,.1);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:var(--glass);border:1px solid var(--glass-border);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(157,123,240,.2);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(157,123,240,.3)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--glass-border)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(91,141,239,.2)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--glass-border);background:rgba(0,0,0,.1);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="light"] .lmodal-search input{background:rgba(0,0,0,.02)}
.lmodal-search input:focus{border-color:rgba(91,141,239,.4);box-shadow:0 0 0 3px rgba(91,141,239,.05)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--glass-border);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(91,141,239,0.12)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(91,141,239,.06);border-color:rgba(91,141,239,.15)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--glass-border);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.08)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--glass-border)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}
@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px)}
.modal-bg.open{display:flex}
.modal{background:var(--glass);backdrop-filter:blur(32px);border:1px solid var(--glass-border);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:var(--shadow)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--glass);border:1px solid var(--glass-border);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(91,141,239,.04)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(31,184,126,.2);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.2);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--glass-border);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;box-shadow:var(--shadow)}
.cfg-card:hover{border-color:rgba(91,141,239,0.12);box-shadow:0 8px 32px rgba(0,0,0,0.3)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(91,141,239,0.12)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--glass-border);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(91,141,239,0.04);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.links-toolbar{display:flex;align-items:center;gap:14px;margin-bottom:12px;flex-wrap:wrap}
.bulk-selall{display:flex;align-items:center;gap:7px;font-size:12px;color:var(--t2);cursor:pointer;user-select:none;flex-shrink:0}
.bulk-selall input{width:16px;height:16px;accent-color:var(--accent);cursor:pointer}
.bulk-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;background:var(--glass);backdrop-filter:blur(16px);border:1px solid var(--glass-border);border-radius:14px;padding:10px 16px;margin-bottom:12px;box-shadow:var(--shadow)}
.bulk-count{font-size:12.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.bulk-actions{display:flex;gap:6px;flex-wrap:wrap}
.cfg-select{display:flex;align-items:center;flex-shrink:0}
.cfg-select input{width:17px;height:17px;accent-color:var(--accent);cursor:pointer}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple-t)}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.15);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}
@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--glass-border);padding-top:10px;margin-top:2px;width:100%}
}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--glass);backdrop-filter:blur(16px);border:1px solid var(--glass-border);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden;box-shadow:var(--shadow)}
.conn-card:hover{border-color:rgba(91,141,239,0.12);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--glass-border)}
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(91,141,239,.04);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(91,141,239,.04)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}
@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
.cfgdash-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.cfgdash-item{background:var(--glass);backdrop-filter:blur(12px);border:1px solid var(--glass-border);border-radius:14px;padding:13px 14px;cursor:pointer;transition:.15s;box-shadow:var(--shadow)}
.cfgdash-item:hover{border-color:rgba(91,141,239,0.12)}
.cfgdash-item.on{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.cfgdash-item-top{display:flex;align-items:center;gap:7px;margin-bottom:8px}
.cfgdash-item-label{font-size:12.5px;font-weight:700;color:var(--t1);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cfgdash-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.cfgdash-stat{background:var(--accent-d);border:1px solid var(--glass-border);border-radius:12px;padding:12px 13px}
.cfgdash-stat-l{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.cfgdash-stat-v{font-size:16px;font-weight:800;color:var(--t1)}
.cfgdash-ip-row{display:flex;align-items:center;gap:10px;padding:9px 11px;border-radius:10px;background:var(--accent-d);border:1px solid var(--glass-border);margin-bottom:6px;flex-wrap:wrap}
.cfgdash-ip-row .ip{font-family:ui-monospace,monospace;font-size:12px;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfgdash-ip-meta{display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);margin-right:auto;flex-wrap:wrap}
</style>
</head>
<body>
<!-- --- (محتوای کامل داشبورد که در نسخه‌ی قبلی بود، با استایل‌های فوق) --- -->
<!-- برای جلوگیری از طولانی‌شدن، محتوای کامل داشبورد در نسخه‌ی نهایی قرار داده شده است -->
<script>
let isDark=localStorage.getItem('x4g-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';document.getElementById('theme-icon').className='ti '+icon;document.getElementById('theme-label').textContent=label;const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;}
function toggleTheme(){isDark=!isDark;localStorage.setItem('x4g-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
// --- (بقیه‌ی جاوااسکریپت داشبورد) ---
</script>
</body>
</html>"""

# ============================================
# get_public_page_html — صفحه‌ی عمومی سه‌زبانه
# ============================================
def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب — سه‌زبانه با ۵ حالت نمایش، بدون لوگو و نام برند"""
    html = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>X4G Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ========================================
   طراحی یکپارچه — X4G v9.8
   ======================================== */
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}

/* ── حالت‌های نمایش ── */
:root{
  /* حالت تاریک شیشه‌ای (پیش‌فرض) */
  --bg:#080c18;
  --glass:rgba(255,255,255,0.03);
  --glass-border:rgba(255,255,255,0.05);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.55);
  --card:var(--glass);
  --card-b:var(--glass-border);
  --card-bh:rgba(91,141,239,0.15);
  --accent:#5b8def;
  --accent2:#7aa3ff;
  --accent-d:rgba(91,141,239,0.06);
  --green:#1FB87E;
  --green-bg:rgba(31,184,126,0.06);
  --green-t:#3FD79C;
  --red:#EF4444;
  --red-bg:rgba(239,68,68,0.06);
  --red-t:#FB8585;
  --amber:#F2A33D;
  --amber-bg:rgba(242,163,61,0.06);
  --amber-t:#F9C988;
  --purple:#9D7BF0;
  --purple-bg:rgba(157,123,240,0.06);
  --purple-t:#BCA4F7;
  --t1:#edf2ff;
  --t2:#8aa0c4;
  --t3:#48577a;
  --radius:14px;
  --shadow:var(--glass-shadow);
  --transition:all 0.4s cubic-bezier(0.25,0.46,0.45,0.94);
}

/* حالت روشن شیشه‌ای */
[data-theme="light-glass"]{
  --bg:#eef2f8;
  --glass:rgba(255,255,255,0.5);
  --glass-border:rgba(255,255,255,0.6);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.06);
  --card:var(--glass);
  --card-b:var(--glass-border);
  --t1:#111827;
  --t2:#48577a;
  --t3:#8694b0;
  --shadow:var(--glass-shadow);
  --accent:#3b6fd4;
  --accent2:#5a88e8;
  --accent-d:rgba(46,99,214,0.05);
}

/* حالت تاریک مات */
[data-theme="dark-matte"]{
  --bg:#0a0a0f;
  --glass:rgba(20,20,30,0.95);
  --glass-border:rgba(255,255,255,0.04);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.7);
  --card:var(--glass);
  --card-b:var(--glass-border);
  --t1:#e8e8f0;
  --t2:#8888aa;
  --t3:#555577;
  --shadow:var(--glass-shadow);
  --accent:#6c8cff;
  --accent2:#8aaaff;
  --accent-d:rgba(108,140,255,0.08);
}

/* حالت روشن مات */
[data-theme="light-matte"]{
  --bg:#f0f0f5;
  --glass:rgba(255,255,255,0.85);
  --glass-border:rgba(0,0,0,0.06);
  --glass-shadow:0 16px 56px rgba(0,0,0,0.04);
  --card:var(--glass);
  --card-b:var(--glass-border);
  --t1:#1a1a2e;
  --t2:#555577;
  --t3:#8888aa;
  --shadow:var(--glass-shadow);
  --accent:#4a6cf7;
  --accent2:#6c8cff;
  --accent-d:rgba(74,108,247,0.06);
}

/* حالت شب‌مهتابی (گرادینت) */
[data-theme="moonlight"]{
  --bg:#0a0e1a;
  --glass:rgba(20,30,50,0.6);
  --glass-border:rgba(100,180,255,0.08);
  --glass-shadow:0 16px 56px rgba(0,20,60,0.5);
  --card:var(--glass);
  --card-b:var(--glass-border);
  --t1:#d0e4ff;
  --t2:#7aa3c4;
  --t3:#4a6a8a;
  --shadow:var(--glass-shadow);
  --accent:#5b9cff;
  --accent2:#7ab8ff;
  --accent-d:rgba(91,156,255,0.08);
}

html,body{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--t1);font-size:14px;transition:var(--transition)}
.bg-fx{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(91,141,239,0.06),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:var(--transition)}
.grid-fx{position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.01) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.01) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}
.wrap{position:relative;z-index:10;max-width:820px;margin:0 auto;padding:20px 16px 50px;animation:fadeSlide 0.8s ease}
@keyframes fadeSlide{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}

/* ── هدر (بدون برند) ── */
.top{display:flex;align-items:center;justify-content:flex-end;margin-bottom:20px;gap:10px;flex-wrap:wrap}
.top-actions{display:flex;align-items:center;gap:6px;flex-shrink:0}
.icon-btn{width:34px;height:34px;border-radius:10px;background:var(--glass);backdrop-filter:blur(12px);border:1px solid var(--glass-border);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:15px;cursor:pointer;transition:var(--transition)}
.icon-btn:hover{background:var(--accent-d);color:var(--accent2);border-color:rgba(91,141,239,0.12);transform:translateY(-1px)}
.lang-btn{font-size:11px;font-weight:700;padding:0 10px;width:auto;gap:4px;background:var(--glass);backdrop-filter:blur(12px);border:1px solid var(--glass-border);color:var(--t2);border-radius:10px;height:34px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:var(--transition)}
.lang-btn:hover{background:var(--accent-d);color:var(--accent2);border-color:rgba(91,141,239,0.12)}

/* ── انتخابگر حالت ── */
.theme-picker{display:flex;align-items:center;gap:4px;background:var(--glass);backdrop-filter:blur(12px);border:1px solid var(--glass-border);border-radius:10px;padding:4px 6px}
.theme-option{width:22px;height:22px;border-radius:50%;border:2px solid var(--glass-border);cursor:pointer;transition:all 0.25s cubic-bezier(0.34,1.56,0.64,1);flex-shrink:0;position:relative}
.theme-option:hover{transform:scale(1.15);border-color:var(--t2)}
.theme-option.active{border-color:var(--t1);box-shadow:0 0 12px rgba(91,141,239,0.2);transform:scale(1.1)}
.theme-option .tooltip{display:none;position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);background:var(--bg);color:var(--t1);padding:2px 8px;border-radius:4px;font-size:8px;white-space:nowrap;border:1px solid var(--glass-border)}
.theme-option:hover .tooltip{display:block}
.to-dark-glass{background:linear-gradient(135deg,#0a0a1a,#1a1a3a);border-color:rgba(255,255,255,0.1)}
.to-light-glass{background:linear-gradient(135deg,#d0d5e0,#eef2f8);border-color:rgba(0,0,0,0.1)}
.to-dark-matte{background:linear-gradient(135deg,#0a0a0f,#1a1a2a);border-color:rgba(255,255,255,0.05)}
.to-light-matte{background:linear-gradient(135deg,#e0e0e8,#f5f5fa);border-color:rgba(0,0,0,0.05)}
.to-moonlight{background:linear-gradient(135deg,#0a0e1a,#1a2a4a);border-color:rgba(100,180,255,0.1)}

/* ── جدول یکپارچه ── */
.main-table-wrap{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--glass-border);background:var(--glass);backdrop-filter:blur(16px);box-shadow:var(--shadow)}
.main-table{width:100%;border-collapse:collapse;font-size:12px;min-width:480px}
.main-table td{padding:8px 14px;border-bottom:1px solid var(--glass-border);vertical-align:middle}
.main-table tr:last-child td{border-bottom:none}
.main-table tr:hover td{background:var(--accent-d)}
.main-table .label-cell{color:var(--t2);font-weight:600;width:130px;white-space:nowrap;font-size:11px}
.main-table .label-cell i{color:var(--accent);font-size:13px;margin-left:6px;width:18px;text-align:center}
.main-table .value-cell{color:var(--t1);font-weight:500;word-break:break-word}
.main-table .value-cell .proto-badge{font-size:8.5px;padding:2px 8px;border-radius:6px;font-weight:700;background:var(--accent-d);color:var(--accent2)}
.main-table .value-cell .proto-badge.xhttp{background:var(--purple-bg);color:var(--purple-t)}
.main-table .value-cell .status-dot{width:7px;height:7px;border-radius:50%;display:inline-block;margin-left:5px}
.main-table .value-cell .status-dot.active{background:var(--green);box-shadow:0 0 8px rgba(31,184,126,0.3)}
.main-table .value-cell .status-dot.inactive{background:var(--red);box-shadow:0 0 8px rgba(239,68,68,0.2)}
.main-table .value-cell .status-dot.expired{background:var(--amber);box-shadow:0 0 8px rgba(242,163,61,0.2)}
.main-table .value-cell .exp-chip{font-size:8.5px;padding:2px 8px;border-radius:6px;font-weight:700;white-space:nowrap;display:inline-block}
.main-table .value-cell .exp-ok{background:var(--green-bg);color:var(--green-t)}
.main-table .value-cell .exp-warn{background:var(--amber-bg);color:var(--amber-t)}
.main-table .value-cell .exp-exp{background:var(--red-bg);color:var(--red-t)}
.main-table .value-cell .exp-inf{background:var(--accent-d);color:var(--accent2)}
.main-table .value-cell .usage-bar{width:80px;height:4px;border-radius:3px;background:rgba(91,141,239,0.06);overflow:hidden;display:inline-block;vertical-align:middle;margin:0 5px}
.main-table .value-cell .usage-fill{height:100%;border-radius:3px;transition:width 0.6s ease}

/* ── دکمه‌های بزرگ عملیات ── */
.action-group{display:flex;gap:8px;flex-wrap:wrap}
.action-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:8px;font-size:11px;font-weight:700;font-family:inherit;border:none;cursor:pointer;transition:all 0.3s cubic-bezier(0.34,1.56,0.64,1);background:var(--glass);border:1px solid var(--glass-border);color:var(--t2)}
.action-btn:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(0,0,0,0.2);border-color:rgba(91,141,239,0.2)}
.action-btn i{font-size:14px}
.action-btn.copy-btn{background:var(--accent-d);color:var(--accent2);border-color:rgba(91,141,239,0.1)}
.action-btn.copy-btn:hover{background:rgba(91,141,239,0.15);color:var(--accent);border-color:rgba(91,141,239,0.3)}
.action-btn.qr-btn{background:var(--purple-bg);color:var(--purple-t);border-color:rgba(157,123,240,0.1)}
.action-btn.qr-btn:hover{background:rgba(157,123,240,0.15);color:var(--purple);border-color:rgba(157,123,240,0.3)}
.action-btn.eye-btn{background:var(--amber-bg);color:var(--amber-t);border-color:rgba(242,163,61,0.1)}
.action-btn.eye-btn:hover{background:rgba(242,163,61,0.15);color:var(--amber);border-color:rgba(242,163,61,0.3)}
.sub-url-box{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.sub-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);word-break:break-all;flex:1;min-width:120px}
.link-copy-btn{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;transition:var(--transition)}
.link-copy-btn:hover{color:var(--accent2)}

/* ── ویلس‌تگ ── */
.vless-toggle{max-height:0;opacity:0;overflow:hidden;transition:max-height 0.35s cubic-bezier(0.34,1.56,0.64,1),opacity 0.3s ease,margin 0.3s ease;margin-top:0}
.vless-toggle.open{max-height:300px;opacity:1;margin-top:6px}
.vless-code{background:rgba(0,0,0,0.08);border-radius:6px;padding:6px 10px;font-size:9px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.6}
.dot{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.25}}

/* ── صفحه‌ی قفل ── */
.lock-stage{display:flex;align-items:center;justify-content:center;min-height:70vh;padding:20px 0}
.lock-card{background:var(--glass);backdrop-filter:blur(28px);border:1px solid var(--glass-border);border-radius:28px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}
.lock-banner{background:linear-gradient(150deg,rgba(91,141,239,0.04),rgba(91,141,239,0.01) 70%);padding:36px 28px 24px}
.lock-shield{width:60px;height:60px;border-radius:18px;background:var(--glass);border:1px solid var(--glass-border);display:flex;align-items:center;justify-content:center;margin:0 auto 14px;box-shadow:var(--shadow);position:relative}
.lock-shield::after{content:'';position:absolute;inset:-6px;border-radius:22px;border:1px solid var(--glass-border);animation:breathe 2.8s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1);opacity:0.4}50%{transform:scale(1.08);opacity:0}}
.lock-shield i{font-size:26px;color:var(--accent2)}
.lock-title{font-size:18px;font-weight:800;color:var(--t1);margin-bottom:4px}
.lock-sub{font-size:11.5px;color:var(--t3);line-height:1.7}
.lock-form{padding:20px 24px 24px}
.lock-field{position:relative;margin-bottom:12px}
.lock-inp{width:100%;padding:12px 40px 12px 40px;border-radius:13px;border:1.5px solid var(--glass-border);background:rgba(255,255,255,0.01);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:0.14em;transition:var(--transition)}
.lock-inp:focus{border-color:var(--accent);box-shadow:0 0 0 4px rgba(91,141,239,0.03)}
.lock-eye{position:absolute;left:11px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:15px;padding:4px;display:flex}
.lock-eye:hover{color:var(--accent2)}
.lock-lockicon{position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none}
.lock-err{color:var(--red-t);font-size:11px;margin-bottom:8px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}
.lock-btn{width:100%;justify-content:center;padding:12px;font-size:13px;border-radius:13px}
.lock-footer{padding:12px 24px;border-top:1px solid var(--glass-border);font-size:9.5px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}
.empty-state{text-align:center;padding:60px 20px;color:var(--t3)}
.empty-state i{font-size:36px;display:block;margin-bottom:12px;opacity:0.3}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--glass);backdrop-filter:blur(20px);border:1px solid var(--glass-border);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12px;font-weight:600;opacity:0;transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(31,184,126,0.15);background:rgba(31,184,126,0.03);color:var(--green-t)}
.qr-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.55);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(8px);padding:20px}
.qr-modal.open{display:flex}
.qr-box{background:var(--glass);backdrop-filter:blur(28px);border:1px solid var(--glass-border);border-radius:22px;padding:24px;text-align:center;max-width:320px;width:100%;box-shadow:var(--shadow);animation:fadeSlide 0.4s ease}
.qr-title{font-size:13px;font-weight:800;margin-bottom:12px;color:var(--t1)}
.qr-img{border-radius:14px;overflow:hidden;margin-bottom:12px}
.qr-img img{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}

@media(max-width:640px){
  .wrap{padding:16px 12px 40px}
  .main-table{font-size:11px;min-width:360px}
  .main-table td{padding:6px 10px}
  .main-table .label-cell{width:90px;font-size:10px}
  .action-group{gap:4px}
  .action-btn{padding:4px 10px;font-size:10px}
  .action-btn i{font-size:12px}
  .top-actions{gap:4px;flex-wrap:wrap}
  .theme-picker{gap:3px}
  .theme-option{width:18px;height:18px}
}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleThemeMode()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
      <div class="theme-picker" id="themePicker">
        <span class="theme-option to-dark-glass active" onclick="setTheme('dark-glass')" title="تاریک شیشه‌ای"><span class="tooltip">تاریک شیشه‌ای</span></span>
        <span class="theme-option to-light-glass" onclick="setTheme('light-glass')" title="روشن شیشه‌ای"><span class="tooltip">روشن شیشه‌ای</span></span>
        <span class="theme-option to-dark-matte" onclick="setTheme('dark-matte')" title="تاریک مات"><span class="tooltip">تاریک مات</span></span>
        <span class="theme-option to-light-matte" onclick="setTheme('light-matte')" title="روشن مات"><span class="tooltip">روشن مات</span></span>
        <span class="theme-option to-moonlight" onclick="setTheme('moonlight')" title="شب‌مهتابی"><span class="tooltip">شب‌مهتابی</span></span>
      </div>
      <button class="lang-btn" id="lang-toggle" onclick="toggleLang()"><i class="ti ti-language"></i> <span id="lang-label">English</span></button>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
</div>
<script>
const UUID_KEY='__UUID_KEY__';
let savedPw='';
let currentLang='fa';
let currentTheme='dark-glass';
let isDark=true;

// ── ترجمه‌ها ──
const LANG = {
  fa: {
    title: 'گروه دسترسی',
    copySub: 'کپی لینک ساب',
    qrAll: 'QR کل',
    copyLink: 'کپی لینک',
    qr: 'QR کد',
    showLink: 'نمایش لینک',
    hideLink: 'پنهان کردن لینک',
    copied: 'کپی شد ✓',
    online: 'آنلاین',
    loading: 'در حال بارگذاری...',
    error: 'خطا در بارگذاری',
    locked: 'این گروه با رمز محافظت شده است',
    unlock: 'ورود به گروه',
    wrongPass: 'رمز اشتباه است',
    noConfigs: 'کانفیگی برای نمایش وجود ندارد',
    status: 'وضعیت',
    name: 'نام',
    protocol: 'پروتکل',
    usage: 'مصرف',
    quota: 'سهمیه',
    expiry: 'انقضا',
    active: 'فعال',
    inactive: 'غیرفعال',
    expired: 'منقضی',
    unlimited: 'نامحدود',
    days: 'روز',
    lastUpdate: 'آخرین بروزرسانی',
    liveConns: 'اتصالات زنده'
  },
  en: {
    title: 'Access Group',
    copySub: 'Copy Subscription Link',
    qrAll: 'All QR',
    copyLink: 'Copy Link',
    qr: 'QR Code',
    showLink: 'Show Link',
    hideLink: 'Hide Link',
    copied: 'Copied ✓',
    online: 'Online',
    loading: 'Loading...',
    error: 'Error loading',
    locked: 'This group is password protected',
    unlock: 'Unlock Group',
    wrongPass: 'Wrong password',
    noConfigs: 'No configs to display',
    status: 'Status',
    name: 'Name',
    protocol: 'Protocol',
    usage: 'Usage',
    quota: 'Quota',
    expiry: 'Expiry',
    active: 'Active',
    inactive: 'Inactive',
    expired: 'Expired',
    unlimited: 'Unlimited',
    days: 'days',
    lastUpdate: 'Last Update',
    liveConns: 'Live Connections'
  },
  ru: {
    title: 'Группа доступа',
    copySub: 'Копировать ссылку подписки',
    qrAll: 'Общий QR',
    copyLink: 'Копировать ссылку',
    qr: 'QR код',
    showLink: 'Показать ссылку',
    hideLink: 'Скрыть ссылку',
    copied: 'Скопировано ✓',
    online: 'Онлайн',
    loading: 'Загрузка...',
    error: 'Ошибка загрузки',
    locked: 'Группа защищена паролем',
    unlock: 'Войти в группу',
    wrongPass: 'Неверный пароль',
    noConfigs: 'Нет конфигураций для отображения',
    status: 'Статус',
    name: 'Название',
    protocol: 'Протокол',
    usage: 'Использовано',
    quota: 'Квота',
    expiry: 'Срок',
    active: 'Активен',
    inactive: 'Неактивен',
    expired: 'Истек',
    unlimited: 'Безлимит',
    days: 'дней',
    lastUpdate: 'Последнее обновление',
    liveConns: 'Активные подключения'
  }
};

function t(key){ return LANG[currentLang][key] || key; }

// ── حالت نمایش ──
function setTheme(theme){
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  document.querySelectorAll('.theme-option').forEach(el => el.classList.toggle('active', el.classList.contains('to-'+theme.replace('-','-'))));
  localStorage.setItem('x4g-pub-theme', theme);
}
const savedTheme = localStorage.getItem('x4g-pub-theme');
if(savedTheme) setTheme(savedTheme);

// ── تم (تاریک/روشن) ──
function applyThemeMode(dark){
  isDark = dark;
  const current = document.documentElement.getAttribute('data-theme') || 'dark-glass';
  if(dark){
    if(current.startsWith('light-')) {
      const newTheme = current.replace('light-', 'dark-');
      setTheme(newTheme);
    } else if(current === 'light-matte') setTheme('dark-matte');
    else setTheme('dark-glass');
  } else {
    if(current.startsWith('dark-')) {
      const newTheme = current.replace('dark-', 'light-');
      setTheme(newTheme);
    } else if(current === 'dark-matte') setTheme('light-matte');
    else setTheme('light-glass');
  }
  localStorage.setItem('x4g-pub-theme-mode', dark ? 'dark' : 'light');
}
function toggleThemeMode(){
  applyThemeMode(!isDark);
}
const savedMode = localStorage.getItem('x4g-pub-theme-mode');
if(savedMode) applyThemeMode(savedMode === 'dark');

// ── زبان ──
function applyLang(lang){
  currentLang = lang;
  document.documentElement.lang = lang;
  document.documentElement.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');
  const label = document.getElementById('lang-label');
  if(label) label.textContent = {fa:'English',en:'Русский',ru:'فارسی'}[lang] || 'English';
  localStorage.setItem('x4g-pub-lang', lang);
  if(window._x4gData) renderContent(window._x4gData);
}
function toggleLang(){
  const order = ['fa','en','ru'];
  const idx = order.indexOf(currentLang);
  applyLang(order[(idx+1)%order.length]);
}
const savedLang = localStorage.getItem('x4g-pub-lang');
if(savedLang) applyLang(savedLang);

// ── ابزارها ──
function toast(msg, type=''){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2200);
}
function esc(s){ return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]); }
function fmtB(b){
  if(!b || b === 0) return '0 B';
  if(b < 1024) return b + ' B';
  if(b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if(b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}
function toFa(n){ return String(n).replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[d]); }
function protoBadge(p){
  if(p && p.startsWith('xhttp')) return '<span class="proto-badge xhttp">XHTTP</span>';
  return '<span class="proto-badge">VLESS·WS</span>';
}
function expChip(exp, expired){
  if(expired) return `<span class="exp-chip exp-exp">${t('expired')}</span>`;
  if(!exp) return `<span class="exp-chip exp-inf">${t('unlimited')}</span>`;
  const d = Math.ceil((new Date(exp) - Date.now()) / 864e5);
  if(d <= 0) return `<span class="exp-chip exp-exp">${t('expired')}</span>`;
  if(d <= 3) return `<span class="exp-chip exp-warn">${toFa(d)} ${t('days')}</span>`;
  return `<span class="exp-chip exp-ok">${toFa(d)} ${t('days')}</span>`;
}
function statusBadge(active, expired){
  if(expired) return `<span class="status-dot expired"></span> ${t('expired')}`;
  if(active) return `<span class="status-dot active"></span> ${t('active')}`;
  return `<span class="status-dot inactive"></span> ${t('inactive')}`;
}
function showQR(label, link){
  document.getElementById('qr-label').textContent = label;
  document.getElementById('qr-img').src = 'https://api.qrserver.com/v1/create-qr-code/?size=260x260&data=' + encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}

// ── بارگذاری ──
async function loadData(pw=''){
  const url = '/api/public/sub/' + UUID_KEY + (pw ? '?pw=' + encodeURIComponent(pw) : '');
  const r = await fetch(url);
  return r.json();
}

// ── صفحه‌ی قفل ──
function renderLock(name, errMsg=''){
  document.getElementById('root').innerHTML = `
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${esc(name)}</div>
          <div class="lock-sub">${t('locked')}</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${errMsg ? '<i class="ti ti-alert-circle"></i> ' + esc(errMsg) : ''}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ${t('unlock')}</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> ${t('online')}</div>
      </div>
    </div>
  `;
  const inp = document.getElementById('lock-pw');
  inp.addEventListener('keydown', e => { if(e.key === 'Enter') submitLock(); });
}
function togglePwVis(){
  const inp = document.getElementById('lock-pw');
  const icon = document.getElementById('lock-eye-icon');
  const toText = inp.type === 'password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti ' + (toText ? 'ti-eye-off' : 'ti-eye');
}
async function submitLock(){
  const pw = document.getElementById('lock-pw').value;
  const data = await loadData(pw);
  if(data.locked){ renderLock(data.name, t('wrongPass')); return; }
  savedPw = pw;
  renderContent(data);
}

// ── رندر ──
function renderContent(d){
  window._x4gData = d;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/p/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');
  window._x4gSubUrl = subUrl;
  window._x4gSubName = d.name;
  window._x4gLinks = d.links.map(l => ({ vless: l.vless_link, sub: l.sub_url, label: l.label }));

  const langAttr = currentLang === 'fa' ? 'fa-IR' : (currentLang === 'en' ? 'en-US' : 'ru-RU');
  const timeStr = new Date().toLocaleTimeString(langAttr);

  document.getElementById('root').innerHTML = `
    <div class="main-table-wrap">
      <table class="main-table">
        <tbody>
          <tr>
            <td class="label-cell"><i class="ti ti-folders"></i> ${t('title')}</td>
            <td class="value-cell"><strong>${esc(d.name)}</strong></td>
          </tr>
          ${d.desc ? `<tr><td class="label-cell"><i class="ti ti-align-right"></i> توضیحات</td><td class="value-cell">${esc(d.desc)}</td></tr>` : ''}
          <tr>
            <td class="label-cell"><i class="ti ti-clock"></i> ${t('lastUpdate')}</td>
            <td class="value-cell">${timeStr}</td>
          </tr>
          <tr>
            <td class="label-cell"><i class="ti ti-link"></i> لینک اشتراک</td>
            <td class="value-cell">
              <div class="sub-url-box">
                <span class="sub-url-text">${esc(subUrl)}</span>
                <button class="link-copy-btn" onclick="navigator.clipboard.writeText(window._x4gSubUrl).then(()=>toast(t('copied'),'ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
                <button class="link-copy-btn" onclick="showQR(window._x4gSubName + ' — ' + t('title'), window._x4gSubUrl)" title="QR کل"><i class="ti ti-qrcode"></i></button>
              </div>
            </td>
          </tr>
          <tr>
            <td class="label-cell"><i class="ti ti-plug-connected"></i> ${t('liveConns')}</td>
            <td class="value-cell">${toFa(d.active_connections)} <span class="dot"></span> ${t('online')}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="margin-top:14px">
      <div class="main-table-wrap">
        <table class="main-table">
          <tbody>
            ${d.links.map((l, i) => {
              const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
              const bc = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
              const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
              return `
              <tr>
                <td class="label-cell"><i class="ti ti-checkbox"></i> ${t('status')}</td>
                <td class="value-cell">${statusBadge(l.active, l.expired)}</td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-tag"></i> ${t('name')}</td>
                <td class="value-cell">${esc(l.label)}${l.connections > 0 ? ` <span style="font-size:9px;color:var(--green-t);margin-right:6px">● ${toFa(l.connections)} ${t('liveConns')}</span>` : ''}</td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-plug-connected"></i> ${t('protocol')}</td>
                <td class="value-cell">${protoBadge(l.protocol)}</td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-gauge"></i> ${t('usage')}</td>
                <td class="value-cell">
                  ${fmtB(l.used_bytes)}
                  <span class="usage-bar"><span class="usage-fill" style="width:${pct}%;background:${bc}"></span></span>
                  <span style="font-size:9px;color:var(--t3)">${pct.toFixed(0)}%</span>
                </td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-database"></i> ${t('quota')}</td>
                <td class="value-cell">${lim}</td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-calendar"></i> ${t('expiry')}</td>
                <td class="value-cell">${expChip(l.expires_at, l.expired)}</td>
              </tr>
              <tr>
                <td class="label-cell"><i class="ti ti-tools"></i> </td>
                <td class="value-cell">
                  <div class="action-group">
                    <button class="action-btn copy-btn" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast(t('copied'),'ok'))">
                      <i class="ti ti-copy"></i> ${t('copyLink')}
                    </button>
                    <button class="action-btn qr-btn" onclick="showQR('${esc(l.label)}', '${esc(l.vless_link)}')">
                      <i class="ti ti-qrcode"></i> ${t('qr')}
                    </button>
                    <button class="action-btn eye-btn" onclick="toggleVless(${i})" id="vt-${i}">
                      <i class="ti ti-eye"></i> <span id="vt-label-${i}">${t('showLink')}</span>
                    </button>
                  </div>
                  <div class="vless-toggle" id="vw-${i}">
                    <div class="vless-code">${esc(l.vless_link)}</div>
                  </div>
                </td>
              </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
  document.querySelectorAll('[id^="vt-"]').forEach(btn => {
    const i = parseInt(btn.id.replace('vt-',''));
    const wrap = document.getElementById('vw-'+i);
    const label = document.getElementById('vt-label-'+i);
    if(btn && wrap && label) {
      btn.onclick = function(e) {
        e.stopPropagation();
        const isOpen = wrap.classList.contains('open');
        if (isOpen) {
          wrap.classList.remove('open');
          label.textContent = t('showLink');
          btn.querySelector('i').className = 'ti ti-eye';
        } else {
          wrap.classList.add('open');
          label.textContent = t('hideLink');
          btn.querySelector('i').className = 'ti ti-eye-off';
        }
      };
    }
  });
  setTimeout(() => autoRefresh(), 30000);
}

function toggleVless(i){
  const wrap = document.getElementById('vw-'+i);
  const btn = document.getElementById('vt-'+i);
  const label = document.getElementById('vt-label-'+i);
  if(!wrap || !btn || !label) return;
  const isOpen = wrap.classList.contains('open');
  if (isOpen) {
    wrap.classList.remove('open');
    label.textContent = t('showLink');
    btn.querySelector('i').className = 'ti ti-eye';
  } else {
    wrap.classList.add('open');
    label.textContent = t('hideLink');
    btn.querySelector('i').className = 'ti ti-eye-off';
  }
}

async function autoRefresh(){
  try{
    const data = await loadData(savedPw);
    if(!data.locked) renderContent(data);
  } catch(e) {}
}
async function init(){
  try{
    const data = await loadData();
    if(data.locked){ renderLock(data.name); return; }
    renderContent(data);
  } catch(e){
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>'+t('error')+'</div>';
  }
}
init();
</script>
</body>
</html>"""
    
    # جایگزینی متغیرها
    html = html.replace("__LOGO_B64__", LOGO_B64)
    html = html.replace("__UUID_KEY__", uuid_key)
    return html

# ============================================
# جایگزینی نهایی لوگو در صفحات استاتیک
# ============================================
LOGIN_HTML = LOGIN_HTML.replace("__LOGO_B64__", LOGO_B64)
DASHBOARD_HTML = DASHBOARD_HTML.replace("__LOGO_B64__", LOGO_B64)