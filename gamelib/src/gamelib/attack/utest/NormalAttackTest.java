package gamelib.attack.utest;

import gamelib.attack.*;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

/**
 * @author chenzq
 *
 */
public class NormalAttackTest {
  
  /**
   * Test method for {@link gamelib.attack.NormalAttack#launch()}.
   */
  @Test
  public void testLaunch() {
    NormalAttack attack = new NormalAttack(60, 150);
    assertEquals(60, attack.getMinDamage());
    assertEquals(60, attack.getMaxDamage());
    assertEquals(90, attack.launch());
  }

  /**
   * Test method for {@link gamelib.attack.NormalAttack#NormalAttack(int, int)}.
   */
  @Test
  public void testNormalAttackIntInt() {
    NormalAttack attack = new NormalAttack(60, 150);
    assertEquals(60, attack.getMinDamage());
    assertEquals(60, attack.getMaxDamage());
    assertEquals(150, attack.getDamageAmplifier());
  }

  /**
   * Test method for {@link gamelib.attack.NormalAttack#NormalAttack()}.
   */
  @Test
  public void testNormalAttack() {
    NormalAttack attack = new NormalAttack();
    assertEquals(0, attack.getMinDamage());
    assertEquals(0, attack.getMaxDamage());
    assertEquals(100, attack.getDamageAmplifier());
  }

}
