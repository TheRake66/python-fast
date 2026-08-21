export function playSound(
  sound: HTMLAudioElement,
  volume: number = 1,
  loop: boolean = false): HTMLAudioElement {

  const clone = sound.cloneNode() as HTMLAudioElement;
  clone.loop = loop;
  clone.volume = volume;
  clone.play().catch(error => { 
    console.error(error); });
  return clone;
}