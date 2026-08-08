<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>77 Spin Jackpot Game</title>
    <style>
        body { margin: 0; padding: 0; background-color: #0c1b33; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; user-select: none; }
        .game-container { width: 100%; max-width: 420px; height: 100vh; background: linear-gradient(180deg, #38bdf8 0%, #1e3a8a 50%, #061124 100%); display: flex; flex-direction: column; justify-content: space-between; padding: 6px; box-sizing: border-box; position: relative; border: 2px solid #eab308; }
        
        .top-header { display: flex; justify-content: space-between; align-items: center; }
        .top-btns { display: flex; gap: 4px; }
        .icon-btn { background: #9333ea; border: 2px solid #eab308; border-radius: 50%; width: 26px; height: 26px; display: flex; justify-content: center; align-items: center; cursor: pointer; font-weight: bold; font-size: 12px; }
        
        .jackpot-box { text-align: center; background: linear-gradient(180deg, #db2777, #9333ea); border: 2px solid #fde047; border-radius: 14px; padding: 2px 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        .jackpot-title { font-size: 11px; font-weight: bold; color: #fde047; text-shadow: 1px 1px 2px #000; letter-spacing: 1px; }
        .jackpot-amount { font-size: 17px; font-weight: bold; color: #fff; text-shadow: 2px 2px 4px #000; }

        .wheel-container { position: relative; width: 240px; height: 240px; margin: 0 auto; display: flex; justify-content: center; align-items: center; }
        .wheel { width: 100%; height: 100%; border-radius: 50%; border: 6px solid #fde047; background: #fbbf24; position: relative; box-shadow: 0 0 20px rgba(251, 191, 36, 0.8); transition: transform 4s cubic-bezier(0.15, 0.9, 0.2, 1); overflow: hidden; }
        
        .wheel-segments {
            width: 100%; height: 100%; border-radius: 50%;
            background: conic-gradient(
                #f97316 0deg 45deg, #3b82f6 45deg 90deg, 
                #f97316 90deg 135deg, #3b82f6 135deg 180deg, 
                #f97316 180deg 225deg, #3b82f6 225deg 270deg, 
                #f97316 270deg 315deg, #3b82f6 315deg 360deg
            );
        }

        .wheel-items { position: absolute; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; }
        .w-item { position: absolute; font-size: 32px; width: 40px; height: 40px; display: flex; justify-content: center; align-items: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.6); }
        
        .item-0 { top: 10%; left: 50%; transform: translateX(-50%); }          
        .item-1 { top: 20%; right: 20%; }                                    
        .item-2 { top: 50%; right: 6%; transform: translateY(-50%); }        
        .item-3 { bottom: 20%; right: 20%; }                                 
        .item-4 { bottom: 10%; left: 50%; transform: translateX(-50%); }     
        .item-5 { bottom: 20%; left: 20%; }                                  
        .item-6 { top: 50%; left: 6%; transform: translateY(-50%); }         
        .item-7 { top: 20%; left: 20%; }                                     

        .wheel-pointer { 
            position: absolute; 
            top: -16px; 
            left: 50%; 
            transform: translateX(-50%); 
            width: 0; 
            height: 0; 
            border-left: 12px solid transparent; 
            border-right: 12px solid transparent; 
            border-top: 24px solid #ef4444; 
            z-index: 20; 
            filter: drop-shadow(0 2px 3px rgba(0,0,0,0.6)); 
        }

        .center-timer { position: absolute; width: 52px; height: 52px; background: linear-gradient(135deg, #9333ea, #c084fc); border-radius: 50%; border: 3px solid #fff; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 0 10px #9333ea; z-index: 10; }
        .timer-text { font-size: 15px; font-weight: bold; color: #fff; text-shadow: 1px 1px 2px #000; }
        
        .round-badge { background: #b45309; border: 1px solid #fde047; padding: 1px 12px; border-radius: 10px; font-size: 11px; font-weight: bold; color: #fde047; text-align: center; width: fit-content; margin: 0 auto; }

        .bet-grid { display: flex; justify-content: space-between; gap: 4px; }
        .bet-card { background: linear-gradient(180deg, #8b5cf6, #6d28d9); border: 2px solid #c084fc; border-radius: 10px; width: 32%; text-align: center; padding: 4px 2px; cursor: pointer; box-shadow: 0 3px 6px rgba(0,0,0,0.4); transition: all 0.2s; position: relative; }
        .bet-card.active { border-color: #22c55e; box-shadow: 0 0 10px #22c55e; transform: scale(1.02); background: linear-gradient(180deg, #15803d, #166534); }
        
        .bet-selected-text { font-size: 9px; color: #fde047; font-weight: bold; margin-bottom: 1px; }
        .bet-icon { font-size: 20px; margin: 1px 0; }
        .bet-mult { font-size: 10px; font-weight: bold; color: #fff; background: rgba(0,0,0,0.3); border-radius: 6px; padding: 1px 5px; display: inline-block; }
        
        .hand-pointer { position: absolute; bottom: 2px; right: 2px; font-size: 14px; animation: bounce 1s infinite; display: none; }
        .bet-card.active .hand-pointer { display: block; }
        @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }

        .result-container { display: flex; align-items: center; background: rgba(0,0,0,0.4); padding: 3px; border-radius: 8px; border: 1px solid #9333ea; gap: 4px; }
        .result-label { background: linear-gradient(90deg, #9333ea, #db2777); padding: 2px 6px; border-radius: 6px; font-size: 10px; font-weight: bold; color: #fde047; border: 1px solid #fde047; }
        .history-bar { display: flex; align-items: center; gap: 4px; overflow-x: auto; white-space: nowrap; width: 100%; }
        .history-bar::-webkit-scrollbar { display: none; }
        .history-item { width: 20px; height: 20px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 10px; background: #3b82f6; border: 1px solid #fff; flex-shrink: 0; }
        .history-item.watermelon { background: #ef4444; }
        .history-item.lucky7 { background: #eab308; color: #000; font-weight: bold; }
        .history-item.grape { background: #8b5cf6; }

        .chip-bar { display: flex; justify-content: space-around; background: rgba(0,0,0,0.4); padding: 3px; align-items: center; border-radius: 8px; border: 1px solid #9333ea; }
        .chip { width: 30px; height: 30px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 8px; cursor: pointer; border: 2px dashed #fff; color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.5); }
        .chip.c1k { background: #3b82f6; }
        .chip.c10k { background: #10b981; }
        .chip.c50k { background: #f59e0b; }
        .chip.c100k { background: #8b5cf6; }
        .chip.c200k { background: #ec4899; }
        .chip.active { border-style: solid; border-color: #fde047; transform: scale(1.1); box-shadow: 0 0 8px #fde047; }

        .footer-info { display: flex; justify-content: space-between; align-items: center; font-size: 10px; padding: 2px 4px; background: rgba(0,0,0,0.6); border-radius: 6px; }
    </style>
</head>
<body>

    <div class="game-container">
        <div class="top-header">
            <div class="top-btns">
                <div class="icon-btn">📄</div>
                <div class="icon-btn">🎵</div>
            </div>
            <div class="jackpot-box">
                <div class="jackpot-title">77 Spin JACKPOT</div>
                <div class="jackpot-amount">46,393,264</div>
            </div>
            <div class="top-btns">
                <div class="icon-btn">?</div>
                <div class="icon-btn">✕</div>
            </div>
        </div>

        <div class="wheel-container">
            <div class="wheel-pointer"></div>
            <div class="wheel" id="wheel">
                <div class="wheel-segments"></div>
                <div class="wheel-items">
                    <div class="w-item item-0">🎰</div>
                    <div class="w-item item-1">🍉</div>
                    <div class="w-item item-2">🍇</div>
                    <div class="w-item item-3">🍉</div>
                    <div class="w-item item-4">🍇</div>
                    <div class="w-item item-5">🍉</div>
                    <div class="w-item item-6">🍇</div>
                    <div class="w-item item-7">🍉</div>
                </div>
            </div>
            <div class="center-timer">
                <span class="timer-text" id="timerDisplay">20s</span>
            </div>
        </div>

        <div class="round-badge" id="roundDisplay">Round: 718</div>

        <div class="bet-grid">
            <div class="bet-card" id="betWatermelon" onclick="selectBet('watermelon')">
                <div class="bet-selected-text">Selected: <span id="selWatermelon">0</span></div>
                <div class="bet-icon">🍉</div>
                <div class="bet-mult">x2</div>
                <div class="hand-pointer">👆</div>
            </div>
            <div class="bet-card active" id="betLucky7" onclick="selectBet('lucky7')">
                <div class="bet-selected-text">Selected: <span id="selLucky7">0</span></div>
                <div class="bet-icon">🎰</div>
                <div class="bet-mult">x8</div>
                <div class="hand-pointer">👆</div>
            </div>
            <div class="bet-card" id="betGrape" onclick="selectBet('grape')">
                <div class="bet-selected-text">Selected: <span id="selGrape">0</span></div>
                <div class="bet-icon"🧇</div>
                <div class="bet-mult">x2</div>
                <div class="hand-pointer">👆</div>
            </div>
        </div>

        <div class="result-container">
            <div class="result-label">Result</div>
            <div class="history-bar" id="historyBar">
                <div class="history-item watermelon">🍉</div>
                <div class="history-item lucky7">77</div>
                <div class="history-item grape">🍇</div>
            </div>
        </div>

        <div class="footer-info">
            <div>Gold Coins: <span style="color: #fde047; font-weight: bold;">7,911</span></div>
            <div>Today's Earnings: <span style="color: #22c55e; font-weight: bold;">0</span></div>
        </div>

        <div class="chip-bar">
            <div class="chip c1k active" onclick="selectChip(this, '1K')">1K</div>
            <div class="chip c10k" onclick="selectChip(this, '10K')">10K</div>
            <div class="chip c50k" onclick="selectChip(this, '50K')">50K</div>
            <div class="chip c100k" onclick="selectChip(this, '100K')">100K</div>
            <div class="chip c200k" onclick="selectChip(this, '200K')">200K</div>
        </div>
    </div>

    <script>
        let timeLeft = 20; // টাইমার ২০ সেকেন্ড সেট করা হয়েছে
        let roundNum = 718;
        let timerInterval = null;
        let isSpinning = false;
        let currentSelectedBet = 'lucky7';
        let currentChip = '1K';

        let spinCount = 0;
        const lucky7TargetSpin = 720; 

        let bets = { watermelon: 0, lucky7: 0, grape: 0 };

        const timerDisplay = document.getElementById('timerDisplay');
        const roundDisplay = document.getElementById('roundDisplay');
        const wheel = document.getElementById('wheel');
        const historyBar = document.getElementById('historyBar');

        const wheelSlots = [
            { type: 'lucky7', emoji: '77' },    // 0
            { type: 'watermelon', emoji: '🍉' },// 1
            { type: 'grape', emoji: '🍇' },      // 2
            { type: 'watermelon', emoji: '🍉' },// 3
            { type: 'grape', emoji: '🍇' },      // 4
            { type: 'watermelon', emoji: '🍉' },// 5
            { type: 'grape', emoji: '🍇' },      // 6
            { type: 'watermelon', emoji: '🍉' } // 7
        ];

        function selectBet(type) {
            currentSelectedBet = type;
            document.getElementById('betWatermelon').classList.remove('active');
            document.getElementById('betLucky7').classList.remove('active');
            document.getElementById('betGrape').classList.remove('active');

            let chipVal = getChipValue(currentChip);

            if (type === 'watermelon') {
                document.getElementById('betWatermelon').classList.add('active');
                bets.watermelon += chipVal;
                document.getElementById('selWatermelon').innerText = formatNumber(bets.watermelon);
            } else if (type === 'lucky7') {
                document.getElementById('betLucky7').classList.add('active');
                bets.lucky7 += chipVal;
                document.getElementById('selLucky7').innerText = formatNumber(bets.lucky7);
            } else if (type === 'grape') {
                document.getElementById('betGrape').classList.add('active');
                bets.grape += chipVal;
                document.getElementById('selGrape').innerText = formatNumber(bets.grape);
            }
        }

        function selectChip(element, val) {
            document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
            element.classList.add('active');
            currentChip = val;
        }

        function getChipValue(chip) {
            if (chip === '1K') return 1000;
            if (chip === '10K') return 10000;
            if (chip === '50K') return 50000;
            if (chip === '100K') return 100000;
            if (chip === '200K') return 200000;
            return 1000;
        }

        function formatNumber(num) {
            if (num >= 1000) return (num / 1000).toFixed(0) + 'K';
            return num;
        }

        function startTimer() {
            timeLeft = 20; // প্রতিবার টাইমার রিসেট হলে ২০ সেকেন্ড থেকে শুরু হবে
            timerDisplay.innerText = timeLeft + 's';
            isSpinning = false;

            if (timerInterval) clearInterval(timerInterval);

            timerInterval = setInterval(() => {
                timeLeft--;
                timerDisplay.innerText = timeLeft + 's';

                if (timeLeft <= 0 && !isSpinning) {
                    clearInterval(timerInterval);
                    spinWheelAndWin();
                }
            }, 1000);
        }

        function spinWheelAndWin() {
            isSpinning = true;
            spinCount++;

            let winningIndex;
            if (spinCount >= lucky7TargetSpin) {
                winningIndex = 0; 
                spinCount = 0; 
            } else {
                winningIndex = Math.floor(Math.random() * 7) + 1;
            }

            let degreesPerSlot = 360 / wheelSlots.length;
            let targetDegree = 1800 + (360 - (winningIndex * degreesPerSlot));

            wheel.style.transform = `rotate(${targetDegree}deg)`;

            setTimeout(() => {
                let winningItem = wheelSlots[winningIndex];
                addHistory(winningItem.type, winningItem.emoji);

                roundNum++;
                roundDisplay.innerText = 'Round: ' + roundNum;

                wheel.style.transition = 'none';
                wheel.style.transform = 'rotate(0deg)';
                
                setTimeout(() => { 
                    wheel.style.transition = 'transform 4s cubic-bezier(0.15, 0.9, 0.2, 1)'; 
                    startTimer();
                }, 50);

            }, 4200);
        }

        function addHistory(type, emoji) {
            const item = document.createElement('div');
            item.className = 'history-item';
            if (type === 'watermelon') {
                item.classList.add('watermelon');
            } else if (type === 'lucky7') {
                item.classList.add('lucky7');
            } else if (type === 'grape') {
                item.classList.add('grape');
            }
            item.innerText = emoji;
            historyBar.appendChild(item);
            historyBar.scrollLeft = historyBar.scrollWidth;
        }

        startTimer();
    </script>

</body>
</html
