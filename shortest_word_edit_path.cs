using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

class HelloWorld
{
  static int ShortestWordEditPath(string source, string target, string[] words) 
  {
    // O(NK) where N is number of words and k is length of words
    // (but probably not) target may not be in array of words -- could *possibly optimize here.
    var distance = new Dictionary<string, int>();
    var queue = new Queue<string>();
    queue.Enqueue(source);
    distance.Add(source, 0);
    while(queue.Any())
    {
      var word = queue.Dequeue();
      
      if(word == target) 
        return distance[word];
      
      foreach(var childWord in words)
      {
        if(!distance.ContainsKey(childWord) && IsChild(word, childWord))
        {
          queue.Enqueue(childWord);
          distance.Add(childWord, distance[word] + 1);
          // Could be worth removing word from list (convert array to list or set) so we don't keep iterating over visited children. 
        }
      }      
    }
    
    return -1;
	}
  
  static bool IsChild(string source, string target)
  {
    if(source.Length != target.Length) 
      return false;
    
    int differences = 0;
    for(int i = 0; i < source.Length; ++i)
    {
      if(source[i] != target[i])
        differences++;
      
      if(differences > 1)
        return false;
    }
    
    return differences == 1;
  }
  
    static void Main()
    {
        var source = "bit";
        var target = "dog";
        var words = new [] {"but", "put", "big", "pot", "pog", "dog", "lot"};
        int len = ShortestWordEditPath(source, target, words);
        // output should be 5: bit -> but -> put -> pot -> pog -> dog
      
      Console.WriteLine($"Shortest length is: {len}.");
    }
}