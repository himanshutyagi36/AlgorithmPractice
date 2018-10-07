import java.util.ArrayList;

class HashNode<K,V> {
	K key;
	V value;
	HashNode<K,V> next; // linked list to store keys
	// Constructor 
    public HashNode(K key, V value) 
    { 
        this.key = key; 
        this.value = value; 
    } 
}

//Class to represent entire hash table
public class HashTable<K,V> {
	// bucket array to store chains
	private ArrayList<HashNode<K,V>> bucketArray = new ArrayList<>();
	
	// current capacity of the array list
	private int numBuckets;
	
	// current size of array list
	private int size;
	
	//constructor
	public HashTable() {
		bucketArray = new ArrayList<>();
		numBuckets = 10;
		size = 0;
		
		// create empty chains
		for (int i=0;i<numBuckets;i++) {
			bucketArray.add(null);
		}
	}
	
	public int getSize() {
		return size;
	}
	
	public boolean isEmpty() {
		return getSize() == 0;
	}
	
	// implement hash function to find 
	// index for a key
	private int getBucketIndex(K key) {
		int hashCode = key.hashCode();
		int index = hashCode % numBuckets;
		return index;
	}
	
	// method to remove key
	private V remove(K key) {
		// get index in hash table
		int bucketIndex = getBucketIndex(key);
		HashNode<K,V> head = bucketArray.get(bucketIndex);
		// search for key in the linke list
		HashNode<K,V> prev = null;
		while(head != null) {
			if(head.key.equals(key))
				break;
			else
				// Else keep moving in chain 
	            prev = head; 
	            head = head.next; 
		}
		
		// if key not present in the linkedlist
		if (head == null)
			return null;
		
		// reduce size
		size--;
		
		// remove key
		if (prev != null)
			prev.next = head.next;
		else
			bucketArray.set(bucketIndex, head.next);
		return head.value;
	}
	
	// get value for a key
	private V get(K key) {
		// Find head of chain for given key 
        int bucketIndex = getBucketIndex(key); 
        HashNode<K, V> head = bucketArray.get(bucketIndex); 
        
        // search key in chain
        while(head != null) {
        	if (head.key.equals(key))
        		return head.value;
        	head = head.next;
        	
        }
        // if key is not found
        return null;
	}
	
	// add key,value to the table
	private void add(K key, V value) {
		// Find head of chain for given key 
        int bucketIndex = getBucketIndex(key); 
        HashNode<K, V> head = bucketArray.get(bucketIndex); 
        
        // check if already existing
        while (head!= null) {
        	// if eists update the value
        	if (head.key.equals(key)){
        		head.value = value;
        		return;
        	}
        	head = head.next;
        }
        
        // Insert key in chain 
        size++; 
        head = bucketArray.get(bucketIndex); 
        HashNode<K, V> newNode = new HashNode<K, V>(key, value); 
        newNode.next = head; 
        bucketArray.set(bucketIndex, newNode); 
        
        // If load factor goes beyond threshold, then 
        // double hash table size 
        if ((1.0*size)/numBuckets >= 0.7) 
        { 
            ArrayList<HashNode<K, V>> temp = bucketArray; 
            bucketArray = new ArrayList<>(); 
            numBuckets = 2 * numBuckets; 
            size = 0; 
            for (int i = 0; i < numBuckets; i++) 
                bucketArray.add(null); 
  
            for (HashNode<K, V> headNode : temp) 
            { 
                while (headNode != null) 
                { 
                    add(headNode.key, headNode.value); 
                    headNode = headNode.next; 
                } 
            } 
        } 
	}
	// Driver method to test Map class 
    public static void main(String[] args) 
    { 
        HashTable<String, Integer>map = new HashTable<>(); 
        map.add("this",1 ); 
        map.add("coder",2 ); 
        map.add("this",4 ); 
        map.add("hi",5 ); 
        System.out.println(map.getSize()); 
        System.out.println(map.remove("this")); 
        System.out.println(map.remove("this")); 
        System.out.println(map.getSize()); 
        System.out.println(map.isEmpty()); 
    } 
}
