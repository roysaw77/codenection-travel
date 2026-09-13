'use strict';
const screen = document.getElementById('screen');
const nav = document.getElementById('app-nav');
const initial = () => ({ role:'child', page:'tours', tour:0, filter:'All tours', sharing:'status', checked:false, alert:'route', large:false, accepted:false });
let state = initial();
const paths = { check:'m5 12 4 4L19 6', arrow:'m9 5 7 7-7 7', back:'m15 5-7 7 7 7', clock:'M12 8v4l3 2 M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0', pin:'M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0 M15 10a3 3 0 1 1-6 0 3 3 0 0 1 6 0', home:'m3 10 9-7 9 7 M5 9v12h5v-7h4v7h5V9', calendar:'M4 5h16v16H4z M8 3v4 M16 3v4 M4 10h16', family:'M8 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8 M2 21v-3a6 6 0 0 1 12 0v3 M17 4a4 4 0 0 1 0 8 M17 15a5 5 0 0 1 5 5v1', phone:'M6 3H3c-1 10 8 19 18 18v-4l-5-2-2 3c-4-2-6-4-8-8l3-2-3-5Z', help:'M12 8v5 M12 17h.01 M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0', walk:'M14 4a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3 M7 10l4-4 4 4 4 1 M11 6l-1 8-4 7 M10 14l6 3v5', shield:'M12 2 3 6v6c0 5 9 10 9 10s9-5 9-10V6z m-5 10 3 3 7-7', rest:'M4 8h13v7a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z M17 9h2a3 3 0 0 1 0 6h-2 M7 2v3 M12 2v3' };
function icon(name){return `<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="${paths[name] || paths.check}"/></svg>`;}
function button(label, action, style='primary', ico=''){return `<button class="action ${style}" data-action="${action}">${ico?icon(ico):''}${label}</button>`;}
function back(to='home'){return `<button class="back" data-action="${to}">${icon('back')}Back</button>`;}
function note(title,text='',style=''){return `<div class="status-note ${style}"><strong>${title}</strong>${text}</div>`;}
function title(name,sub=''){return `<h2>${name}</h2>${sub?`<p class="sub">${sub}</p>`:''}`;}
function escapeText(value){return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
