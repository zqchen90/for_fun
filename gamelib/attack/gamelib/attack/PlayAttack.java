package gamelib.attack;

public class PlayAttack {

  public static void main(String[] args) {
    Attack attack = new RandomAttack(1,100,40,100);
    testAttackTime(attack, 100000);
    /* ---- Test Attack Time ----
     * Repeat 100000000 times, total 1478 ms, average 0.000015 ms 
     */
    
    attack = new NormalAttack(100, 100);
    testAttackTime(attack, 100000);
    /* ---- Test Attack Time ----
     * Repeat 100000000 times, total 103 ms, average 0.000001 ms
     */
    
    RandomAttack rattack = new RandomAttack(10,100,10,100);
    int probability = 0;
    while (probability <= 100) {
      rattack.setProbability(probability);
      testRandomAttackProbability(rattack, 10000000);
      probability += 10;
    }
    /*
     * Test in 2015-5-14
     * Error less than 0.05%
     */
  }
 
  
  public static void testAttackTime(Attack attack, int repeatTimes) {
    System.out.println("---- Test Attack Time ----");
    int i = 0;
    long startTime = System.currentTimeMillis();
    while (i < repeatTimes) {
      attack.launch();
      i++;
    }
    long endTime = System.currentTimeMillis();
    System.out.printf("Repeat %d times, total %d ms, average %f ms \n\n",
                        repeatTimes,
                        endTime - startTime,
                        (endTime - startTime) * 1.0 / repeatTimes);
  }
  
  public static void testRandomAttackProbability(RandomAttack attack, int repeatTimes) {
    System.out.println("---- Test Attack Probability ----");
    int repeatCount = 0;
    int launchCount = 0;
    while (repeatCount < repeatTimes) {
      if (attack.launch() > 0) {
        launchCount++;
      }
      repeatCount++;
    }
    System.out.printf("Repeat %d times, launch %d times, actual p = %5.3f, expect p = %d\n\n",
                        repeatTimes,
                        launchCount,
                        launchCount * 100.0 / repeatTimes,
                        attack.getProbability());
  }

}
