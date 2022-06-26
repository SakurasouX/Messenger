profile_icon.onclick = function() {
    let div = document.createElement('div')
    div.className = 'profile-icon-popup'
    let profile_div = document.querySelector('.profile')
    profile_div.append(div)
    
    if (document.body.onclick) {
        div.remove()
    }
}