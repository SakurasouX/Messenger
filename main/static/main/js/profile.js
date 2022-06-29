profile_icon.onclick = function() {
    let profile_popup = document.querySelector('.profile-icon-popup');
    profile_popup.style.display = 'block';
}

let popup = document.querySelector('.profile-icon-popup');
document.addEventListener('mousedown', function(e){
    if(e.target.closest('.profile-icon-popup') === null){
        popup.style.display = 'none';
    }
});
