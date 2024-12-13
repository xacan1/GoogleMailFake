document.addEventListener('DOMContentLoaded', function () {
	const form = document.getElementById('search')
	const input = document.getElementById('search-input')
	const searchPopup = document.getElementById('search-popup')

	form.addEventListener('submit', e => e.preventDefault())
	input.addEventListener('focus', () => {
		form.classList.add('active')
		searchPopup.classList.add('active')
	})
	input.addEventListener('blur', () => {
		form.classList.remove('active')
		searchPopup.classList.remove('active')
	})

	const menuBtn = document.getElementById('menu')
	const sendBtn = document.getElementById('send')
	const leftBar = document.querySelector('.left-bar')

	leftBar.addEventListener('mouseenter', function () {
		leftBar.classList.add('hovered')
		leftBar.classList.add('active')
		sendBtn.classList.add('hovered-send')
	})

	leftBar.addEventListener('mouseleave', function () {
		leftBar.classList.remove('hovered');

		if (menuBtn.classList.contains('active')) {
			
		} else if (!menuBtn.classList.contains('active-click')){
			leftBar.classList.remove('active');
		}

		sendBtn.classList.remove('hovered-send');
	})

	const newPopup = document.getElementById('new')
	const newClose = document.getElementById('new-close')

	menuBtn.addEventListener('click', function () {
		menuBtn.classList.toggle('active');
		menuBtn.classList.toggle('active-click');
		leftBar.classList.toggle('active');
	})

	sendBtn.addEventListener('click', function () {
		newPopup.classList.toggle('active');
	})

	newClose.addEventListener('click', function () {
		newPopup.classList.remove('active')
	})

	const mails_item = document.querySelectorAll('.item')

	mails_item.forEach(item => {
		item.addEventListener('click', () => {
			mails_item.forEach(t => t.classList.remove('active'))
			item.classList.add('active')
		})
	})
	const inboxTabs = document.querySelectorAll('.inbox-tab')

	inboxTabs.forEach(tab => {
		tab.addEventListener('click', () => {
			inboxTabs.forEach(t => t.classList.remove('active'))
			tab.classList.add('active')
		})
	})

	const account = document.getElementById('account')
	const accountBtn = document.getElementById('account-btn')
	const accountCloseBtn = document.getElementById('account-close-btn')
	const overlay = document.getElementById('overlay')

	accountBtn.addEventListener('click', () => {
		account.classList.add('active')
		overlay.classList.add('active')
	})
	accountCloseBtn.addEventListener('click', () => {
		account.classList.remove('active')
		overlay.classList.remove('active')
	})
	overlay.addEventListener('click', () => {
		account.classList.remove('active')
		overlay.classList.remove('active')
	})

	const message = document.getElementById('message')
	// const content = document.getElementById('content')
	const sticky = document.getElementById('sticky')
	const inboxContent = document.getElementById('inbox-content')
	const contentFooter = document.getElementById('content-footer')
	// const mail = document.getElementById('mail')
	// const back = document.getElementById('back')

	// message.addEventListener('click', () => {
	// 	sticky.style.display = 'none'
	// 	inboxContent.style.display = 'none'
	// 	contentFooter.style.display = 'none'
	// 	mail.style.display = 'block'
	// 	history.pushState(null, '', '/#1')
	// })

	// back.addEventListener('click', () => {
	// 	sticky.style.display = 'flex'
	// 	inboxContent.style.display = 'block'
	// 	contentFooter.style.display = 'block'
	// 	mail.style.display = 'none'
	// 	history.pushState(null, '', '/')
	// })
})
