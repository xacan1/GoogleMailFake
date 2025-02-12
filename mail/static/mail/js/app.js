document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('search');
    const input = document.getElementById('search-input');
    const searchPopup = document.getElementById('search-popup');

    // form.addEventListener('submit', (e) => e.preventDefault());
    input.addEventListener('focus', () => {
        form.classList.add('active');
        searchPopup.classList.add('active');
    });
    input.addEventListener('blur', () => {
        form.classList.remove('active');
        searchPopup.classList.remove('active');
    });

    const menuBtn = document.getElementById('menu');
    const sendBtn = document.getElementById('send');
    const leftBar = document.querySelector('.left-bar');

    const replyBtn1 = document.getElementById('button-reply1');
    const replyBtn2 = document.getElementById('button-reply2');

    leftBar.addEventListener('mouseenter', function () {
        leftBar.classList.add('hovered');
        leftBar.classList.add('active');
        sendBtn.classList.add('hovered-send');
    });

    leftBar.addEventListener('mouseleave', function () {
        leftBar.classList.remove('hovered');

        // if (menuBtn.classList.contains('active')) {
        // } else {
        //     leftBar.classList.remove('active');
        // }

        sendBtn.classList.remove('hovered-send');
    });

    const newPopup = document.getElementById('new');
    const newClose = document.getElementById('new-close');

    const newReplyPopup = document.getElementById('new-reply');

    if (replyBtn1) {
        replyBtn1.addEventListener('click', function () {
            newReplyPopup.classList.toggle('active');
        })
    }

    if (replyBtn2) {
        replyBtn2.addEventListener('click', function () {
            newReplyPopup.classList.toggle('active');
        })
    }

    menuBtn.addEventListener('click', function () {
        menuBtn.classList.toggle('active');
        leftBar.classList.toggle('active');
    });

    sendBtn.addEventListener('click', function () {
        newPopup.classList.toggle('active');
    });

    newClose.addEventListener('click', function () {
        newPopup.classList.remove('active');
        newReplyPopup.classList.remove('active');
    });

    const mails_item = document.querySelectorAll('.item');

    mails_item.forEach((item) => {
        item.addEventListener('click', () => {
            mails_item.forEach((t) => t.classList.remove('active'));
            item.classList.add('active');
        });
    });
    const inboxTabs = document.querySelectorAll('.inbox-tab');

    inboxTabs.forEach((tab) => {
        tab.addEventListener('click', () => {
            inboxTabs.forEach((t) => t.classList.remove('active'));
            tab.classList.add('active');
        });
    });

    const account = document.getElementById('account');
    const accountBtn = document.getElementById('account-btn');
    const accountCloseBtn = document.getElementById('account-close-btn');
    const overlay = document.getElementById('overlay');

    accountBtn.addEventListener('click', () => {
        account.classList.add('active');
        overlay.classList.add('active');
    });
    accountCloseBtn.addEventListener('click', () => {
        account.classList.remove('active');
        overlay.classList.remove('active');
    });
    overlay.addEventListener('click', () => {
        account.classList.remove('active');
        overlay.classList.remove('active');
    });

    // const message = document.getElementById('message');

    // const mail = document.getElementById('mail');
    // const back = document.getElementById('back');

    // const messagesContent = document.querySelector('.messages-content');
    // const messages = document.querySelector('.messages ');

    // message.addEventListener('click', () => {
    //     // sticky.style.display = 'none';
    //     // inboxContent.style.display = 'none';
    //     // contentFooter.style.display = 'none';
    //     messages.style.width = '50%';
    //     messagesContent.style.display = 'flex';
    //     mail.style.display = 'block';
    //     history.pushState(null, '', '/#1');
    // });

    // back.addEventListener('click', () => {
    //     sticky.style.display = 'flex';
    //     inboxContent.style.display = 'block';
    //     contentFooter.style.display = 'block';
    //     mail.style.display = 'none';
    //     history.pushState(null, '', '/');
    // });
    const mailResize = document.querySelector('.new__top-btn.resize');
    const newEmail = document.querySelector('#new');
    const newContainer = document.querySelector('.new-container');
    mailResize.addEventListener('click', () => {
        newEmail.classList.toggle('full_width');
        newContainer.classList.toggle('new_height');
    });
});
