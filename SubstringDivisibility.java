/***********************************************
 * Name: SubstringDivisibility.java
 * Author: Dave, Nick, Marj
 * version: 1.0
 * Date: 2/15/2021
 * description: solution to project euler #43
 * *********************************************/
import java.util.HashMap;
// import java.util.Vector;
// import java.util.ArrayList;
 public class SubstringDivisibility{
     public static boolean checkP(String str){
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i<str.length(); i++){
            char c = str.charAt(i);
            if (map.containsKey(c)){
                return false;
            } else{
                map.put(c,1);
            }
        }
        Object[] keys = map.keySet().toArray();
        int len = str.length();
        int keylen = keys.length;
        if (keylen!=len){
            return false;
        }
        for (int i = 0; i<keylen; i++){
            int key = Integer.parseInt(keys[i].toString());
            if(key>=len || key<0){
                return false;
            }
        }
        return true;
    }
    public static boolean checkProperty(char[] sa){
        int size = sa.length;
        // char[] sa = s.toCharArray();
        if(((sa[3]-'0') % 2) != 0){
            return false;
        }
        if(size>=5){
            if(((sa[2]-'0') + (sa[3]-'0') + (sa[4]-'0'))%3 != 0){
                return false;
            } 
        }
        if(size >= 6){
            //only need to check 6th digit 
            if(((sa[5]-'0') % 5) != 0){
                return false;
            }
        }
        //if size 7 digits 5,6,7 are divisible by 7
        if(size >= 7){
            if((((sa[4]-'0')*100 + (sa[5]-'0')*10 + (sa[6]-'0')) % 7) != 0){
                return false;
            }
        }
        //if size 8 digits 6,7,8 are divisible by 11
        if(size >= 8){
            if((((sa[5]-'0')*100 + (sa[6]-'0')*10 + (sa[7]-'0')) % 11) != 0){
                return false;
            }
        }
        //if size 9 indexes 7,8,9 are divisible by 13
        if(size >= 9){
            if((((sa[6]-'0')*100 + (sa[7]-'0')*10 + (sa[8]-'0')) % 13) != 0){
                return false;
            }
        }
        //if size 10 indexes 8,9,10 are divisible by 17
        if(size == 10){
            if((((sa[7]-'0')*100 + (sa[8]-'0')*10 + (sa[9]-'0')) % 17) != 0){
                return false;
            }
        }
        return true;
    }
    public static long lexicoOrder(int n){
        String s = "";
        for (int i = 0; i<n;i++){
            s+=String.valueOf(i);
        }
        String f = "";
        for (int i = n-1;i>=0;i--){
            f+=String.valueOf(i);
        }
        long sum = 0;
        // Vector<String> v = new Vector<String>();
        if(checkProperty(s.toCharArray())){
            // v.add(s);
            System.out.println(s);
            sum += Long.parseLong(s);
        }
        while(!s.equals(f)){
            int k=0;
            for(int i =s.length()-1; i>0;i--){
                if(s.charAt(i)>s.charAt(i-1)){
                    k=i-1;
                    break;
                }
            }
            int j=0;
            for (int m = s.length()-1; m>k ;m--){
                if(s.charAt(m)>s.charAt(k)){
                    j = m;
                    break;
                }
            }
            char[] sa = s.toCharArray();
            char temp = sa[k];
            sa[k] = sa[j];
            sa[j] = temp;
            s = String.valueOf(sa);
            String s1 = s.substring(0,k+1);
            String s2 = s.substring(k+1);
            s2 = new StringBuilder(s2).reverse().toString();
            s=s1+s2;
            if(checkProperty(s.toCharArray())){
                //v.add(s);
                System.out.println(s);
                sum+=Long.parseLong(s);
            }
        }
        return sum;

    }
    public static void main(String[] args){
        long start = System.nanoTime();
        int strlen = args[0].length();
        // if (strlen<4 || strlen>10){
        //     System.out.println("Invalid input");
        //     System.out.printf("Elapsed time: %.6f ms\n" , (System.nanoTime() - start) / 1e6);
        // }
        // if (!checkP(args[0])){
        //     System.out.println("The number is not a pandigitalnumber");
        //     System.out.printf("Elapsed time: %.6f ms\n" , (System.nanoTime() - start) / 1e6);
        // } else{
        // Vector<String> v = lexicoOrder(strlen);
        // for(int i = 0; i<v.size();i++){
        //     System.out.println(v.get(i));
        //     sum += Long.parseLong(v.get(i));
        // }
        long sum = lexicoOrder(strlen);
        System.out.println(sum);
        System.out.printf("Elapsed time: %.6f ms\n" , (System.nanoTime() - start) / 1e6);
        // }
    }
 }