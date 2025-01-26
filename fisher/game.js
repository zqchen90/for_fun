// 加载游戏资源
const backgroundImage = new Image();
const playerFishImage = new Image();
const smallFishImage = new Image();

backgroundImage.src = 'assets/background.jpg';
playerFishImage.src = 'assets/player-fish.png';
smallFishImage.src = 'assets/small-fish.png';

// 获取游戏元素
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score');

// 游戏状态
let score = 0;
let gameOver = false;

// 玩家鱼的属性
const player = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    size: 30,
    speed: 5
};

// 小鱼数组
let smallFishes = [];

// 鼠标位置
let mouseX = 0;
let mouseY = 0;

// 监听鼠标移动
canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
});

// 生成小鱼
function createSmallFish() {
    const side = Math.floor(Math.random() * 4); // 0:上, 1:右, 2:下, 3:左
    let x, y;
    
    switch(side) {
        case 0: // 上边
            x = Math.random() * canvas.width;
            y = -20;
            break;
        case 1: // 右边
            x = canvas.width + 20;
            y = Math.random() * canvas.height;
            break;
        case 2: // 下边
            x = Math.random() * canvas.width;
            y = canvas.height + 20;
            break;
        case 3: // 左边
            x = -20;
            y = Math.random() * canvas.height;
            break;
    }

    return {
        x,
        y,
        size: Math.max(10, (player.size - 10) + Math.random() * 30), // 基于玩家大小动态生成小鱼大小
        speed: 2 + Math.random() * 2,
        angle: Math.atan2(player.y - y, player.x - x)
    };
}

// 绘制鱼
function drawFish(x, y, size, angle, isPlayer = false) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(angle);
    
        // 绘制鱼的图片
    const image = isPlayer ? playerFishImage : smallFishImage;
    ctx.drawImage(image, -size, -size/2, size * 2, size);
    
    ctx.restore();
}

// 更新游戏状态
function update() {
    if (gameOver) return;

    // 更新玩家位置
    const dx = mouseX - player.x;
    const dy = mouseY - player.y;
    const distance = Math.hypot(dx, dy);
    const angle = Math.atan2(dy, dx);
    
    // 只有当距离大于10像素时才移动
    if (distance > 10) {
        player.x += Math.cos(angle) * Math.min(player.speed, distance);
        player.y += Math.sin(angle) * Math.min(player.speed, distance);
    }

    // 生成新的小鱼
    if (Math.random() < 0.02) {
        smallFishes.push(createSmallFish());
    }

    // 更新小鱼位置
    smallFishes.forEach((fish, index) => {
        fish.x += Math.cos(fish.angle) * fish.speed;
        fish.y += Math.sin(fish.angle) * fish.speed;

        // 检测碰撞
        const distance = Math.hypot(player.x - fish.x, player.y - fish.y);
        if (distance < (player.size + fish.size) / 2) {
            if (player.size > fish.size) {
                // 玩家吃掉小鱼
                score += Math.floor(fish.size);
                scoreElement.textContent = `分数：${score}`;
                smallFishes.splice(index, 1);
                player.size += 0.5; // 玩家变大
            } else {
                // 游戏结束
                gameOver = true;
                setTimeout(() => {
                    alert(`游戏结束！最终得分：${score}`);
                    location.reload();
                }, 100);
            }
        }

        // 移除超出边界的小鱼
        if (fish.x < -50 || fish.x > canvas.width + 50 ||
            fish.y < -50 || fish.y > canvas.height + 50) {
            smallFishes.splice(index, 1);
        }
    });
}

// 绘制游戏画面
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // 绘制背景
    ctx.drawImage(backgroundImage, 0, 0, canvas.width, canvas.height);

    // 绘制玩家
    const playerAngle = Math.atan2(mouseY - player.y, mouseX - player.x);
    drawFish(player.x, player.y, player.size, playerAngle, true);

    // 绘制小鱼
    smallFishes.forEach(fish => {
        drawFish(fish.x, fish.y, fish.size, fish.angle);
    });

    if (gameOver) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fff';
        ctx.font = '48px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('游戏结束', canvas.width/2, canvas.height/2);
    }
}

// 游戏循环
function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// 开始游戏
gameLoop();
// 设置画布大小为全屏
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    // 重新定位玩家到屏幕中央
    player.x = canvas.width / 2;
    player.y = canvas.height / 2;
}

// 初始化时设置画布大小
resizeCanvas();

// 监听窗口大小变化
window.addEventListener('resize', resizeCanvas);